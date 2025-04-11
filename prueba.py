import cv2 #libreria para capturar y procesar imangenes desde la camara 
import mediapipe as mp #libreria para detectar la mano y analizarla 
import tkinter as tk #libreria para la interfaz grafica 
from PIL import Image, ImageTk #para convertir la imagen de OpenCV en un fomrato compatible con tkinter 

#configuracion de MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

#variables para el objeto virtual 
objeto_x, objeto_y = 300, 200
arrastrando = False

#detecciòn de la mano cerrada verifica si al menos 3 de los dedos estan cerrados 
def mano_cerrada(landmarks):
    
    dedos_doblados = 0
    if landmarks.landmark[8].y > landmarks.landmark[6].y:  
        dedos_doblados += 1
    if landmarks.landmark[12].y > landmarks.landmark[10].y:  
        dedos_doblados += 1
    if landmarks.landmark[16].y > landmarks.landmark[14].y:  
        dedos_doblados += 1
    if landmarks.landmark[20].y > landmarks.landmark[18].y:  
        dedos_doblados += 1
    return dedos_doblados >= 3

#captura el video y decta la mano
def actualizar_video():
    global objeto_x, objeto_y, arrastrando

    ret, frame = cap.read()
    if not ret:
        print("No se puede acceder a la camara")
        return

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultados = hands.process(frame_rgb)

    if resultados.multi_hand_landmarks:
        print("Mano detectada")
        for hand_landmarks in resultados.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            alto, ancho, _ = frame.shape
            cx = int(hand_landmarks.landmark[8].x * ancho)
            cy = int(hand_landmarks.landmark[8].y * alto)

            if mano_cerrada(hand_landmarks):
                print("Mano cerrada")
                if abs(cx - objeto_x) < 60 and abs(cy - objeto_y) < 60 or arrastrando:
                    objeto_x, objeto_y = cx, cy
                    arrastrando = True
            else:
                if arrastrando:
                    print("Soltando objeto")
                arrastrando = False

#dibujar el objeto
    cv2.circle(frame, (objeto_x, objeto_y), 40, (255, 0, 0), -1)

#Actualizar la imagen en Tkinter
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    imgtk = ImageTk.PhotoImage(image=img)
    lbl_video.imgtk = imgtk
    lbl_video.configure(image=imgtk)
    lbl_video.after(10, actualizar_video)

#Interfaz grafica con Tkinter
ventana = tk.Tk()
ventana.title("Arrastrar y soltar con mano")
ventana.geometry("800x600")

lbl_video = tk.Label(ventana)
lbl_video.pack()

cap = cv2.VideoCapture(0)
actualizar_video()
ventana.mainloop()
cap.release()