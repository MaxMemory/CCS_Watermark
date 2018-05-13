import cv2
import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageFont, ImageDraw, ImageTk

#IMAGE_1 = Image.open('images/img1.png')
#IMAGE_2 = Image.open('images/img2.png')
#IMAGE_1.show()
#IMAGE_1.paste(IMAGE_2, (0, 0), IMAGE_2)
#IMAGE_1.save('images/img_output.png')


def filedialog_input():
    global file_input, img_input
    global canvas, canvas_width, canvas_height
    file_input = askopenfilename(filetypes=(("Images files", "*.png;*.jpg;*.PNG;*.JPG"),
                                           ("Images files", "*.png;*.jpg;*.PNG;*.JPG") ))
    etr1.insert(0, file_input)
    img_input = tk.PhotoImage(file=file_input)
    calculate_watermark()

def filedialog_watermark():
    global file_WM, img_WM
    global canvas, canvas_width, canvas_height
    global wx, wy
    file_WM = askopenfilename(filetypes=(("Images files", "*.png;*.jpg;*.PNG;*.JPG"),
                                           ("Images files", "*.png;*.jpg;*.PNG;*.JPG") ))
    etr2.insert(0, file_WM)
    img_WM = tk.PhotoImage(file=file_WM)
    calculate_watermark()

def calculate_watermark():
    global wx, wy, tx, ty
    global canvas, canvas_width, canvas_height, img_input, img_WM, file_input, file_WM, scal_x, scal_y, text_input
    global img_test, img1
    # Reset canvas
    canvas.delete("all")
    if (file_input != ''):
        #canvas.create_image(percent(wx, canvas_width),percent(wy, canvas_height), image=img_WM)
        img_pil = write_image()
        #img_pil.show()
        img_tkinter = ImageTk.PhotoImage(img_pil)
        rr = tk.Label(window, image=img_tkinter)
        rr.pack()
        #img_test = tk.PhotoImage(img_tkinter)
        #canvas.create_image( canvas_width, canvas_height, image=img_test)

def saveImage():
    img = write_image()
    img.save('images/img_output_2.png')
        
    
def write_image():
    global img_input, img_WM, file_input, file_WM, text_input, tx, ty, wx, wy, canvas_width, canvas_height
    global font, img1
    img_1 = Image.open(file_input).convert("RGBA")
    width, height = img_1.size
    if (file_WM != ''):
        img_2 = Image.open(file_WM).convert("RGBA")
        img_1.paste( img_2, (percent(wx, width), percent(wy, height)), img_2)
    if (text_input != ''):
        draw = ImageDraw.Draw(img_1)
        draw.text((percent(tx, width), percent(ty, height)), text_input, font=font, fill=(255,255,0))
    #img_1.save('images/img_output_2.png')
    return img_1
    

def percent(p, length):
    return (int)(length*(int(p)/100))

def resize(img, length):
    #width = img.width()
    #height = img.height()
    #scal_x = (img_input.width()/canvas_width) * 100
    #scal_y = (img_input.height()/canvas_height) * 100
    #img = img.resize((scal_y, scal_y), Image.ANTIALIAS)
    return 0

    

def get_wx(val):
    global wx
    wx = val
    calculate_watermark()

def get_wy(val):
    global wy
    wy = val
    calculate_watermark()

def get_tx(val):
    global tx,text_input
    tx = val
    text_input = etr3.get()
    calculate_watermark()

def get_ty(val):
    global ty, text_input
    ty = val
    text_input = etr3.get()
    calculate_watermark()

def get_text_input(val):
    global text_input
    text_input = val
    calculate_watermark()
    

file_input = ''
file_WM = ''
text_input = ''
scal_x = 0.0
scal_y = 0.0
wx = 0
wy = 0
tx = 0
ty = 0
font = ImageFont.truetype('fonts/Nunito-Regular.ttf', 32)

# 240P resolution
canvas_width = 426
canvas_height = 240

# Initialize
window = tk.Tk()
window.title('test')
window.geometry('470x580')
canvas = tk.Canvas( width=canvas_width, height=canvas_height, bg='#888888')
canvas.place(x=20, y=20)



#canvas.create_image(20,20, image=img)
#img = tk.PhotoImage(file='images/img2.png')
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
slider_wx = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=get_wx)
slider_wy = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=get_wy)
slider_tx = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=get_tx)
slider_ty = tk.Scale(window, from_=0, to=100, orient=tk.HORIZONTAL, command=get_ty)
slider_wx.place(x=100, y=387)
slider_wy.place(x=100, y=427)
slider_tx.place(x=340, y=387)
slider_ty.place(x=340, y=427)

# Create Add Watermake Button
btn3 = tk.Button(text='add watermark', font=(8), command=saveImage)
btn3.place(x=170, y=520)

# Create Image
#load_img = tk.PhotoImage(file='images/img1.png')
#img1 = tk.Label(image=load_img)
#img1.image = load_img
#img1.place(x=100, y=100)
window.mainloop()