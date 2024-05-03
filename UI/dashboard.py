from tkinter import *
import main
from view_requests import view_request_status_page
from chat import chat_page

def dashboard_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Dashboard")
    root.geometry('500x300')
    root.configure(bg='#2d2d2d')

    frame = Frame(root, bg='white', bd=5)  # Set background color to white
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Welcome to the Marks Resolution System", bg='white', fg='black', font=('Arial', 20), wraplength=450).pack(pady=10)  # Set background color to white and foreground color to black
    Label(frame, text="Here is how to draft a good request:", bg='white', fg='black', font=('Arial', 20), wraplength=450).pack(pady=10)
    Label(frame, text="You will need a good description of your problem", bg='white', fg='black', font=('Arial', 20), wraplength=450).pack(pady=10)
    
    Label(frame, text="Example:", bg='white', fg='black', font=('Arial', 20), wraplength=450).pack(pady=10)
    Label(frame, text="I received a grade of 70% on my English assignment, but I believe I should have received an 80% because I followed all the guidelines and met all the requirements.", bg='white', fg='black', font=('Arial', 20), wraplength=450).pack(pady=10)
    Label(frame, text="If scripts are available, provide them, as this will facilitate the process.", bg='white', fg='black', font=('Arial', 20), wraplength=450).pack(pady=10)

    view_request_status_button = Button(frame, text="View Request Status", bg='black', fg='white', font=('Arial', 20), command=lambda: view_request_status_page(root))
    view_request_status_button.pack(pady=20)

    new_request_button = Button(frame, text="New Request", bg='black', fg='white', font=('Arial', 20), command=lambda: chat_page(root))
    new_request_button.pack(pady=20)