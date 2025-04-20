import tkinter as tk
GREY = '#D3D3D3'
BLACK = '#000000'

# czyszczenie ekranu
def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()

# instrukcja screen
def create_instruction_menu():
    clear_screen()
    welcome = tk.Label(text='Welcome in the Typing Speed Test!',font=('arial',30,'bold'),fg=GREY,bg=BLACK)
    welcome.grid(row=0,padx=50)

    instruction_label = tk.Label(text='This is program to check Your typing speed'
    '\n1)Choose difficulty.'
    '\n2)Random words will apear'
    '\n3)Start typing , timer will start'
    '\n4)After rewriting whole text test will end, and app will count and provide final results'
    '\n5)Each mistake counts'
    '\n6)Highest score will be saved'
    '\nWPM - Words Per Minute, CPM - Characters per Minute,'
    '\nNET WPN -WPN with counted mistakes',font=('arial',15,'bold'),bg=BLACK,fg=GREY)
    instruction_label.grid(row=1,padx=10,pady=20)

    good_luck = tk.Label(text='Good Luck!',font=('arial',30,'bold'),fg=GREY,bg=BLACK)
    good_luck.grid(row=2)

    # go back button

    back_button = tk.Button(text='Go back',font=('arial',30,'bold'),fg=GREY,bg=BLACK,command=create_menu_screen)
    back_button.grid(row=3)
# Stworzenie Menu screen
def create_menu_screen():
    clear_screen()
    # Title
    menu = tk.Label(window,text='Choose a dificulty', font=('Tahoma',50,'bold'),bg=BLACK,fg=GREY)
    menu.grid(column=0,row=0,pady=30,columnspan=3,sticky='n')

    # instruction
    instruction_button = tk.Button(window,text='Instruction',font=('Helvetica',15,'bold'),bg=BLACK,fg=GREY,command=create_instruction_menu)
    instruction_button.grid(row=1,column=1)
    # Easy button
    easy_button = tk.Button(window,text='Easy',font=('Helvetica',30,'bold'),bg=BLACK,fg='green')
    easy_button.grid(row=2,column=0,padx=50,sticky='e')

    # Hard button
    hard_button = tk.Button(window,text='Hard',font=('Helvetica',30,'bold'),bg=BLACK,fg='red')
    hard_button.grid(row=2,column=2,padx=50,sticky='w')





# Set window,
window = tk.Tk()
window.title('Writing Speed Test')

# Color
window.config(background='black',pady=10,padx=10)

create_menu_screen()

















# window loop stay opened
window.mainloop()