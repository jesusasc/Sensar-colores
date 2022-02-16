from pickletools import uint1, uint8
from tkinter import Frame
import cv2
import numpy as np

#Sensar color mediante la camara 
#Rango y color para sensar

colorin = np.array([33,0,0], np.uint8)
colorfi = np.array([63,255,255], np.uint8)

cam = cv2.VideoCapture(0)

while True:
    ban, frameBGR = cam.read()
    #invertir la camara y que no se vea como espejo 
    frameBGR = cv2.flip(frameBGR,1)

    #Converitir imagen de BGR a HSV
    frameHSV = cv2.cvtColor(frameBGR,cv2.COLOR_BGR2HSV)

    #Detectar colores 
    detecta = cv2.inRange(frameHSV, colorin, colorfi)



    #Condicion para mostrar la fotograma 
    if ban == True:
        cv2.imshow("Camara On", frameBGR)
        cv2.imshow("Camara HSV", frameHSV)
        cv2.imshow("Camara Detectar", detecta)
        #Condicion para apagar la camara 
        if cv2.waitKey(1) & 0xFF == ord('a'):
            break

cam.release()
cv2.destroyAllWindows()