import numpy as np
import cv2
import matplotlib.pyplot as ptl
import random as rnd
import os


pic_num=0

def shuffle_array(num):
    global sa
    sa = np.arange(num+1)
    rnd.shuffle(sa)
    #sa = np.copy(shuffle_array)

def generateCircles(num):
    
    if not os.path.exists('After'):
        os.makedirs('After')
    if not os.path.exists('Before'):
        os.makedirs('Before')
        
    a = []
    for i in range(num):
        a.append(((rnd.random()*i)/(i+rnd.random()))%127)

    bg1 = np.ones((256,256,3),dtype = "uint8")*255
    bg2 = np.ones((256,256,3),dtype = "uint8")*255
    bg3 = np.ones((256,256,3),dtype = "uint8")*255

    posx=1
    posy=1
    global pic_num
    
    for x in a:
        posx = int(((x*1000)+41)%(147+x*(posy)))#+(247+posy)))
        posy = int(((x*1000)+37)%(127+x*(posx)))#+(227+posx)))
        rad = int(((x*97+47)/100)*(max(posx,posy)))%195
        if rad<=3:
            rad = 33
        cv2.circle(bg1,(posx,posy),rad,(0,0,0),3)
        cv2.circle(bg2,(posx,posy),rad,(0,0,0),3)
        cv2.circle(bg2,(posx,posy),(rad-2),(92,24,255),-1)
##        cv2.imshow('bg1'+'_'+str(i),bg1)
##        cv2.imshow('bg2'+'_'+str(i),bg2)
        cv2.imwrite("Before/"+"Img_bef_"+str(sa[pic_num])+'.jpg',bg1)
        cv2.imwrite("After/"+"Img_aft_"+str(sa[pic_num])+'.jpg',bg2)
        pic_num += 1
        bg1 = np.copy(bg3)
        bg2 = np.copy(bg3)
        
    print(pic_num)
        
               

def generateRectangles(num):
    
    if not os.path.exists('After'):
        os.makedirs('After')
    if not os.path.exists('Before'):
        os.makedirs('Before')
        
    a = []
    for i in range(num):
        a.append(((rnd.random()*i)/(i+rnd.random()))%127)

    bg1 = np.ones((256,256,3),dtype = "uint8")*255
    bg2 = np.ones((256,256,3),dtype = "uint8")*255
    bg3 = np.ones((256,256,3),dtype = "uint8")*255

    posx=1
    posy=1
    global pic_num
        
    for x in a:
        posx = int(((x*1000)+41)%(147+x*(posy)))#+(247+posy)))
        posy = int(((x*1000)+37)%(127+x*(posx)))#+(227+posx)))
        widthx = int(((x*97+47)/100)*(max(posx,posy)))%149
        widthy = int(1000/(widthx+2))%113
        if widthx<=3:
            widthx = 33
        if widthy<=3:
            widthy = 33

        cv2.rectangle(bg1,(posx-widthx,posy-widthy),(posx+widthy,posy+widthx),(0,0,0),3)
        cv2.rectangle(bg2,(posx-widthx,posy-widthy),(posx+widthy,posy+widthx),(0,0,0),3)
        cv2.rectangle(bg2,(posx-widthx+2,posy-widthy+2),(posx+widthy-2,posy+widthx-2),(92,24,255),-1)
        cv2.imwrite("Before/"+"Img_bef_"+str(sa[pic_num])+'.jpg',bg1)
        cv2.imwrite("After/"+"Img_aft_"+str(sa[pic_num])+'.jpg',bg2)
        pic_num += 1
        bg1 = np.copy(bg3)
        bg2 = np.copy(bg3)
        
    print(pic_num)



def generateEllipse(num):
    
    if not os.path.exists('After'):
        os.makedirs('After')
    if not os.path.exists('Before'):
        os.makedirs('Before')
        
    a = []
    for i in range(num):
        a.append(((rnd.random()*i)/(i+rnd.random()))%127)

    bg1 = np.ones((256,256,3),dtype = "uint8")*255
    bg2 = np.ones((256,256,3),dtype = "uint8")*255
    bg3 = np.ones((256,256,3),dtype = "uint8")*255

    posx=1
    posy=1
    global pic_num
        
    for x in a:
        #print(x)
        posx = int(x*103 + (1-x)*157)#int(((x*1000)+41)%(98+x*(posy)))#+(247+posy)))
        posy = int(x*157 + (1-x)*103)#int(((x*1000)+37)%(93+x*(posx)))#+(227+posx)))
        widthx = int(((x*97+47)/100)*(max(posx,posy)))%100
        widthy = int(1000/(widthx+2))%85
        #print("X=",widthx," Y=",widthy)
        if widthx<=3:
            widthx = 67
        if widthy<=3:
            widthy = 93
        cv2.ellipse(bg1,(posx,posy),(widthx,widthy),int(x*100),0,360,(0,0,0),3)
        cv2.ellipse(bg2,(posx,posy),(widthx,widthy),int(x*100),0,360,(0,0,0),3)
        cv2.ellipse(bg2,(posx,posy),(widthx-2,widthy-2),int(x*100),0,360,(92,24,255),-1)
##        cv2.imshow('Img1'+str(pic_num),bg1)
##        cv2.imshow('Img2'+str(pic_num),bg2)
        cv2.imwrite("Before/"+"Img_bef_"+str(sa[pic_num])+'.jpg',bg1)
        cv2.imwrite("After/"+"Img_aft_"+str(sa[pic_num])+'.jpg',bg2)
        pic_num += 1
        bg1 = np.copy(bg3)
        bg2 = np.copy(bg3)

    print(pic_num)

def generateShapes(num):
    shuffle_array(num)
    noi = int(num/3)
    generateCircles(noi)
    generateRectangles(noi)
    generateEllipse(noi)
    print(pic_num)

print(pic_num)



