import tkinter as tk
from PIL import ImageTk, Image,ImageDraw,ImageFont
from tkinter import filedialog, font, ttk

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
    height = image.height - 50
    size = (width,height)
    # SCALE
    scale_value = int(scale.get())
    print(scale_value)
    # IMG
    
    text_to_add = entry.get()
    text_font = ImageFont.truetype("arial.ttf",scale_value)
    edit_image = ImageDraw.Draw(image)


    edit_image.text(size,text_to_add,('red'),font=text_font)
    IMAGE = image
    photo2 = ImageTk.PhotoImage(image)
    image_label.config(image=photo2)
    image_label.photo2 = photo2

def save_photo():
    IMAGE.save('czapka.png')

# window
window = tk.Tk()

# Button OpenFile
button = tk.Button(text="Open File",command=open_file)
button.grid(row=1)

# Image
image_label = tk.Label(window)
image_label.grid(row=0,column=0)


# Settings
frame = tk.Frame(window)
frame.config(borderwidth=2,relief='solid',padx=10, pady=10,)
frame.grid(row=0,column=1,sticky='n')

# Entry
entry = tk.Entry(frame)
entry.pack(padx=5,pady=5)
entry.insert(0,'Your text')


# Font 
choices = font.names()
choice = ttk.Combobox(frame,textvariable='pupa')
choice.config(values=choices)
choice.set('Font choice')
choice.pack(padx=5,pady=5)

# Scale

scale = ttk.Scale(frame,orient='vertical',length=50,from_=1,to=60)
scale.bind('<Motion>',set_text)
scale.pack()

# ready button
OK_button = tk.Button(frame,text="Try",command=set_text)
OK_button.pack(padx=5,pady=5)

save_button = tk.Button(frame,text='Save',command=save_photo)
save_button.pack()

window.mainloop()