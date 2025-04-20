import tkinter as tk
from PIL import ImageTk, Image,ImageDraw,ImageFont
from tkinter import filedialog, font, ttk
import os
PATH = 'file'
IMAGE = 'd'
# Open image
def open_file():
    global PATH
    filename = filedialog.askopenfilename(title='Open Image File')
    if filename:
        PATH = filename
        display_photo(filename)
        

# Display image
def display_photo(filename):
    photo = Image.open(filename)
    image = ImageTk.PhotoImage(photo)
    image_label.config(image=image)
    image_label.image = image
# set text

def set_text(event):
    global IMAGE
    image = Image.open(PATH)

    # SIZE OF IMAGE
    width = image.width - 200
    height = image.height - 25
    size = (width,height)
    # SCALE
    scale_value = int(scale.get())
    print(scale_value)
    # IMG
    
    text_to_add = entry.get()
    text_font = ImageFont.truetype(selected_font.get(),scale_value)
    edit_image = ImageDraw.Draw(image)

    bbox = edit_image.textbbox((0, 0), text_to_add, font=text_font)
    text_width = bbox[2] - bbox[0]  
    text_height = bbox[3] - bbox[1]
    # position and put image
    selected = selected_position.get()
    if selected == 'top_left':
        position = (0,0)
    elif selected == 'bottom_left':
        position = (0,height - text_height)
    elif selected == 'top_right':
        position = (image.width- text_width,0)
    elif selected == 'bottom_right':
        position = (image.width- text_width,height - text_height)
    elif selected == 'bottom_left':
        position = (0,height - text_height)
    edit_image.text(position,text_to_add,('red'),font=text_font)

    IMAGE = image
    photo2 = ImageTk.PhotoImage(image)
    image_label.config(image=photo2)
    image_label.photo2 = photo2

def save_photo():
    IMAGE.save('czapka.png')

# window
window = tk.Tk()
window.geometry('800x600')

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=0)
window.columnconfigure(2, weight=0) 
window.rowconfigure(1, weight=1)
# Button OpenFile
button = tk.Button(text="Open File",command=open_file)
button.grid(row=1,column=2,sticky='se')

# Image
image_label = tk.Label(window)
image_label.grid(row=0,column=0)


# Settings
frame = tk.Frame(window)
frame.config(borderwidth=2,relief='solid',padx=10, pady=10,)
frame.grid(row=0,column=2,sticky='ne')

# Entry
entry = tk.Entry(frame)
entry.pack(padx=5,pady=5)
entry.insert(0,'Your text')


# Font 
selected_font = tk.StringVar()
font_dir = "C:/Windows/Fonts"  # lub odpowiednia ścieżka na twoim systemie
fonts = [f for f in os.listdir(font_dir) if f.lower().endswith(".ttf")]
choices = fonts
choice = ttk.Combobox(frame,textvariable=selected_font)
choice.config(values=choices)
choice.set('arial.ttf')
choice.pack(padx=5,pady=5)
# Position

selected_position = tk.StringVar()
selected_position.set('top_left')
top_left = tk.Radiobutton(frame,text='top left',variable=selected_position,value='top_left')
top_left.pack()

top_right = tk.Radiobutton(frame,text='top right',variable=selected_position,value='top_right')
top_right.pack()

bottom_left = tk.Radiobutton(frame,text='bottom left',variable=selected_position,value='bottom_left')
bottom_left.pack()

bottom_right = tk.Radiobutton(frame,text='bottom right',variable=selected_position,value='bottom_right')
bottom_right.pack()
print(selected_position.get())


# Scale

scale = ttk.Scale(frame,orient='vertical',length=50,from_=1,to=60)
scale.bind('<Motion>',set_text)
scale.set(25)
scale.pack()

# ready button
OK_button = tk.Button(frame,text="Try",command=set_text)
OK_button.pack(padx=5,pady=5)

save_button = tk.Button(frame,text='Save',command=save_photo)
save_button.pack()

window.mainloop()