import os
import argparse
import cv2

#This function is to be used within a loop the increment 
#represents the individual file the loop will iterate through
#where the file path is path to the file without the quotation marks
#do not inlude the trailing forward slash

img_Array = []

def readFromFile(filepath, increment):
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help="path to the image file", default=f'{filepath}/{increment}')                
    args = vars(ap.parse_args())
    image = cv2.imread(args["image"])    
    #Outputs a 300 x 300 px image
    #image = cv2.resize(image, (300, 300))
    return image 

def img_array(filepath):
    for file in os.listdir(f'{filepath}/'):
        img_Array.append(readFromFile(filepath, file))
        #This will build an array of the images in the directory

    return img_Array