from tkinter import *
import main

def login_page(root):
    root.title("Login Page")
    root.geometry('500x300')
    root.configure(bg='#2d2d2d')

    canvas = Canvas(root, bg='#2d2d2d', bd=0, highlightthickness=0)
    canvas.place(relx=0.5, rely=0.5, anchor=CENTER)
    canvas.create_rectangle(10, 10, 490, 290, outline='black', fill='white', width=2, smooth=True)

    Label(canvas, text="Your ICT-U Email", bg='white', fg='black', font=('Arial', 20)).place(x=20, y=20)
    email_entry = Entry(canvas, bg='#5F5F5F', fg='white', font=('Arial', 20))
    email_entry.place(x=20, y=60, width=460, height=40)

    login_button = Button(canvas, text="Login", bg='black', fg='white', font=('Arial', 20), command=lambda: main.main_page(root))
    login_button.place(x=20, y=120, width=460, height=40)

root = Tk()
login_page(root)
root.mainloop()