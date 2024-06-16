from tkinter import *
import argparse
import cv2
import os
import numpy as np
from readFromFile import *
from PIL import ImageTk, Image


def readFromFilepath():
    global img
    filepath = Input_img.get()
    if os.path.exists(filepath):
        print("Folder Exists")
        for file in os.listdir(f'{filepath}'):
            img = Image.open(f'{filepath}/{file}')
            img = img.resize((150,150), Image.Resampling.LANCZOS)
            img = ImageTk.PhotoImage(img)
            disp_Img = Label(root,image=img)
            disp_Img.grid(row=7, column=1, columnspan=2)

            display = Label(root, text=f'{filepath}/{file}')
            display.grid(row=8, column=2)
    else:
        print("Problem")

root =Tk()
root.title('Image Viewer')

Input_Label = Label(root, text="Folder Src.").grid(row=1, column=1, pady=10)
Input_img = Entry(root)
Input_img.grid(row=1, column=2, columnspan=6, pady=10)

InputLabel = Label(root, text="Input Upper HSV: ").grid(row=2, column=1)
H1 = Entry(root, width = 10).grid(row=2, column=2, padx=(0,5))
S1 = Entry(root, width = 10).grid(row=2, column=3, padx=(0,5)) 
V1 = Entry(root, width = 10).grid(row=2, column=4, padx=(0,5))
InputLabel = Label(root, text="Input Lower HSV: ").grid(row=4, column=1)
H2 = Entry(root, width = 10).grid(row=4, column=2, padx=(0,5))
S2 = Entry(root, width = 10).grid(row=4, column=3, padx=(0,5)) 
V2 = Entry(root, width = 10).grid(row=4, column=4, padx=(0,5))

show_Img = Button(root, text="Image", command=readFromFilepath).grid(row=5, column=2)

quit_button = Button(root, text="Quit", command=root.quit).grid(row=10, column=5, padx=15, pady=15)
root.mainloop()