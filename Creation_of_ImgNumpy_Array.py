##For Creating a Numpy Array of input images and Output Images
import cv2
import numpy as np
import os
##def load_images(num):
##    aft_list,bef_list = list(),list()
##    for i in range(num+1):
##        imgaft = cv2.imread("After/Img_aft_"+str(i)+'.jpg',1)
##        imgbef = cv2.imread("Before/Img_bef_"+str(i)+'.jpg',1)
##        aft_list.append(imgaft)
##        bef_list.append(imgbef)
##
##    return [np.asarray(aft_list),np.asarray(bef_list)]

def load_images(num):
    aft_list,bef_list = list(),list()
    pathaft = 'After/'
    pathbef = 'Before/'
    count=0
    for filename in os.listdir(pathaft):
        count+=1
        img = cv2.imread(pathaft+filename,1)
        aft_list.append(img)
        if(count>num):
            count=0
            break

    count=0    
    for filename in os.listdir(pathbef):
        count+=1
        img = cv2.imread(pathbef+filename,1)
        bef_list.append(img)
        if(count>num):
            count=0
            break

    return [np.asarray(aft_list),np.asarray(bef_list)]
    


def make_image_array(num):
    [aft_images,bef_images] = load_images(num)
    print('Loaded: ',aft_images.shape,bef_images.shape)
    filename = 'train_images_'+str(num)+'.npz'
    np.savez_compressed(filename,bef_images,aft_images)
    print('Saved dataset: ',filename)




        
