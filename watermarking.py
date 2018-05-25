import tkinter as tk
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageFont, ImageDraw, ImageTk

def filedialog_input():
    global file_input
    global canvas, canvas_width, canvas_height
    file_input = askopenfilename(filetypes=(("Images files", "*.png;*.jpg;*.PNG;*.JPG"),
                                           ("Images files", "*.png;*.jpg;*.PNG;*.JPG") ))
    etr1.insert(0, file_input)
    update_canvas()

def filedialog_watermark():
    global file_WM
    global canvas, canvas_width, canvas_height
    global wx, wy
    file_WM = askopenfilename(filetypes=(("Images files", "*.png;*.jpg;*.PNG;*.JPG"),
                                           ("Images files", "*.png;*.jpg;*.PNG;*.JPG") ))
    etr2.insert(0, file_WM)
    update_canvas()

def update_canvas():
    global wx, wy, tx, ty
    global canvas, canvas_width, canvas_height
    global file_input, file_WM, text_input
    global scal_x, scal_y
    global img_tkinter

    canvas.delete("all")
    if (file_input != ''):
        img_pil = write_image()
        w1, h1 = img_pil.size
        scale_w = canvas_width/w1
        scale_h = canvas_height/h1
        scale = scale_w if scale_w < scale_h else scale_h
        width = (int)(w1*scale)
        height = (int)(h1*scale)
        img_pil = img_pil.resize((width, height))
        img_pil.save('resources/temp.png')
        img_tkinter = tk.PhotoImage(file='resources/temp.png')
        canvas.create_image(  canvas_width/2, canvas_height/2, image=img_tkinter)

def showImage():
    img = write_image()
    img.show()

def saveImage():
    img = write_image()
    img.save('output.png')
        
def write_image():
    global file_input, file_WM, text_input
    global canvas_width, canvas_height
    global tx, ty, wx, wy
    global font
    img_1 = Image.open(file_input)
    width, height = img_1.size
    if (file_WM != ''):
        img_2 = Image.open(file_WM).convert("RGBA")
        img_1.paste( img_2, (percent(wx, width), percent(wy, height)), img_2)
    if (text_input != ''):
        draw = ImageDraw.Draw(img_1)
        draw.text((percent(tx, width), percent(ty, height)), text_input, font=font, fill=(255,255,0))
    return img_1

def percent(p, length):
    return (int)(length*(int(p)/100))

def get_wx(val):
    global wx
    wx = val
    update_canvas()

def get_wy(val):
    global wy
    wy = val
    update_canvas()

def get_tx(val):
    global tx,text_input
    tx = val
    text_input = etr3.get()
    update_canvas()

def get_ty(val):
    global ty, text_input
    ty = val
    text_input = etr3.get()
    update_canvas()

def get_text_input(val):
    global text_input
    text_input = val
    update_canvas()

# 240P resolution
canvas_width = 426
canvas_height = 240

# Initialize
file_input = ''
file_WM = ''
text_input = ''
scal_x = 0.0
scal_y = 0.0
wx = 0
wy = 0
tx = 0
ty = 0
window = tk.Tk()
window.title('test')
window.geometry('470x580')
canvas = tk.Canvas( width=canvas_width, height=canvas_height, bg='#888888')
canvas.place(x=20, y=20)
font = ImageFont.truetype('fonts/Nunito-Regular.ttf', 48)

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

# Create Show Image Button
btn3 = tk.Button(text='Show', font=(8), command=showImage)
btn3.place(x=170, y=520)

# Create Save Image Button
btn4 = tk.Button(text='Save', font=(8), command=saveImage)
btn4.place(x=250, y=520)

window.mainloop()