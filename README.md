Arastrar y soltar con detección de manos 

El proyecto utiliza OpenCV, MediaPipe y Tkinter para detectar una mano mediante 
la camara web y permite el arrastre de un objeto virutal en la pantalla cuando 
la mano esta cerrada.

Caracteristicas 
Detección de manos en tiempo real mediante MediaPipe 
Seguimiento del indice para mover el objeto en la pantalla 
Interfaz grafica con Tkinter
Captura de pantalla mediante Open CV

Requisitos para poder correr el pograma 
tener instaladas las siguientes librerias: pip install opencv-python mediapipe pillow
nota: tener una version de python no mayor a la 3.10 porque algunas librerias ya no 
son compatibles con las versiones de python mayor a la 3.10

como ejecutar el programa 

se puede mediante el comando python main.py  en la teminar 
o ejecutar el progrma en la terminal de visual code 

Notas:
la detencion de la mano se basa en el numero de dedos doblados que como minimo tiene que ser 3 
El objeto cambiara su posición cuando la mano cerrada este cerca de el y se habra 
haciendo la simulacion de que se solto el objeto 
Para sair, cerrar la venta de Tkinter 
