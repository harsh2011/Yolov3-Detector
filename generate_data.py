import cv2
import random
import os
import numpy as np

max_data_images = 2000
crop_min_size = 45
crop_max_size = 60

crop_path = "./crops"
background_path = "./backgrounds"

def getcropslist(crop_path):
    list_of_crops = []
    for path in os.listdir(crop_path):
        list_of_crops.append(crop_path+"/"+path)

    return list_of_crops

def getbackgroundlist(background_path):
    list_of_backgrounds = []
    for path in os.listdir(background_path):
        list_of_backgrounds.append(background_path+"/"+path)

    return list_of_backgrounds

print("Crops:")
list_of_crops = getcropslist(crop_path)
no_of_crops = len(list_of_crops)
print(list_of_crops)
print("Backgrounds:")
list_of_backgrounds = getbackgroundlist(background_path)
no_of_backgrounds = len(list_of_backgrounds)
print(list_of_backgrounds)


tt_f = open("./data/tt_ball.txt", 'w')

i = 0
while(i<max_data_images):


    
    crop = cv2.imread(list_of_crops[random.randrange(no_of_crops)])
    crop = np.array(crop)
    
    background = cv2.imread(list_of_backgrounds[random.randrange(no_of_backgrounds)])
    background = np.array(background)

    # crop
    size = random.randrange(crop_min_size, crop_max_size)
    crop = cv2.resize(crop, (size, size))
    c_height, c_width, _ = crop.shape
    print(crop.shape)

    # background
    b_height, b_width, _ = background.shape

    # height and width difference
    d_height = b_height - c_height
    d_width = b_width - c_width


    # pick out the position
    x = random.randrange(d_width)
    y = random.randrange(d_height)
    
    f = open("./data/other_labels/"+str(i)+".txt", 'w')
    f.write("0 "+str(x)+" "+str(y)+" "+str(c_width)+" "+str(c_height))
    f.close()
    f = open("./data/labels/"+str(i)+".txt", 'w')
    center_x = (x+(c_width/2))/b_width
    center_y = (y+(c_height/2))/b_height
    nor_c_width = c_width/b_width
    nor_c_height = c_height/b_height
    f.write("0 "+str(center_x)+" "+str(center_y)+" "+str(nor_c_width)+" "+str(nor_c_height))
    f.close()
    background[y:y+c_height,x:x+c_width,:] = crop


    cv2.imwrite("./data/images/"+str(i)+".jpg", background)

    tt_f.write("./data/images/"+str(i)+".jpg"+"\n")

    i+=1
    print(i)
    #break
tt_f.close()