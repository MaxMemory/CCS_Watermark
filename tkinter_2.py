import cv2
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image


def filedialog_input():
    filepath = askopenfilename(filetypes=(("Images files", "*.png;*.jpg"),
                                           ("Images files", "*.png;*.jpg") ))
    etr1.insert(0, filepath)
    #return filepath

def filedialog_watermark():
    filepath = askopenfilename(filetypes=(("Images files", "*.png;*.jpg"),
                                           ("Images files", "*.png;*.jpg") ))
    etr2.insert(0, filepath)
    #return filepath

# 240P resolution
canvas_width = 426
canvas_height = 240

# Initialize
window = tk.Tk()
window.title('test')
window.geometry('470x580')
canvas = tk.Canvas( width=canvas_width, height=canvas_height)
canvas.create_rectangle(0, 0, canvas_width, canvas_height, fill="#888888")
canvas.place(x=20, y=20)


#img = tk.PhotoImage(file="images/img1.png")
#canvas.create_image(20,20, image=img)

#Create Input Text
text1 = tk.Label(text='Image:', font=(8))
text1.place(x=20, y=267)

# Create Input Entries
etr1 = tk.Entry(font=(8))
etr1.place(x=125, y=270, width=220)

# Create Button
btn1 = tk.Button(text='load image', font=(6), command=filedialog_input)
btn1.place(x=355, y=265)

# Create WaterMark Text
text2 = tk.Label(text='Watermark:', font=(8))
text2.place(x=20, y=307)

# Create Entries
etr2 = tk.Entry(font=(8))
etr2.place(x=125, y=310, width=220)

# Create Button
btn2 = tk.Button(text='load image', font=(6), command=filedialog_watermark)
btn2.place(x=355, y=305)

# InputText text
text3 = tk.Label(text='Input text:', font=(8))
text3.place(x=20, y=347)

# Create InputText Entries
etr3 = tk.Entry(font=(8))
etr3.place(x=125, y=350, width=100)

# WM Position text
text3 = tk.Label(text='WM pos:', font=(8))
text3.place(x=20, y=387)
# Text Position text
text4 = tk.Label(text='Text pos:', font=(8))
text4.place(x=260, y=387)
#Create Slider
slider_wx = tk.Scale(from_=0, to=426, orient=tk.HORIZONTAL)
slider_wy = tk.Scale(from_=0, to=240, orient=tk.HORIZONTAL)
slider_tx = tk.Scale(from_=0, to=426, orient=tk.HORIZONTAL)
slider_ty = tk.Scale(from_=0, to=240, orient=tk.HORIZONTAL)
slider_wx.place(x=100, y=387)
slider_wy.place(x=100, y=427)
slider_tx.place(x=340, y=387)
slider_ty.place(x=340, y=427)

# Create Add Watermake Button
btn3 = tk.Button(text='add watermark', font=(8))
btn3.place(x=170, y=520)

# Create Image
#load_img = tk.PhotoImage(file='images/img1.png')
#img1 = tk.Label(image=load_img)
#img1.image = load_img
#img1.place(x=100, y=100)
window.mainloop()





