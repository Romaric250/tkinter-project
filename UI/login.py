
from tkinter import *
from tkinter import messagebox
import requests
import json
from dashboard import dashboard_page


def login_page(root):
    root.title("Login Page")
    root.geometry('500x300')
    root.configure(bg='#2d2d2d')

    frame = Frame(root, bg='white', bd=5)  
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Your ICT-U Email", bg='white', fg='black', font=('Arial', 20)).pack(pady=10)  # Set background color to white and foreground color to black
    email_entry = Entry(frame, bg='#5F5F5F', fg='white', font=('Arial', 20))
    email_entry.pack(ipady=10)

    def login():
        email = email_entry.get()
        if not email.endswith("ictuniversity.edu.cm"):
            messagebox.showerror("Error", "Authenticate with your ICT email")
            return

        data = {"email": email}
        response = requests.post("http://localhost:5000/login", json=data)

        if response.status_code == 200:
            messagebox.showinfo("Success", "User logged in successfully.")
            token_page(root)
        else:
            messagebox.showerror("Error", "Failed to login.")

    login_button = Button(frame, text="Login", bg='black', fg='white', font=('Arial', 20), command=login)
    login_button.pack(pady=20)


def token_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Token Verification")
    root.geometry('500x300')
    root.configure(bg='#2d2d2d')

    frame = Frame(root, bg='white', bd=5)  # Set background color to white
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(frame, text="Enter Token", bg='white', fg='black', font=('Arial', 20)).pack(pady=10)  # Set background color to white and foreground color to black
    token_entry = Entry(frame, bg='#5F5F5F', fg='white', font=('Arial', 20))
    token_entry.pack(ipady=10)

    submit_button = Button(frame, text="Submit", bg='black', fg='white', font=('Arial', 20), command=lambda: dashboard_page(root))
    submit_button.pack(pady=20)

    reenter_button = Button(frame, text="Did not receive token, re-enter email", bg='black', fg='white', font=('Arial', 20), command=lambda: login_page(root))
    reenter_button.pack(pady=20)







# from tkinter import *
# import main
# from dashboard import dashboard_page

# def login_page(root):
#     root.title("Login Page")
#     root.geometry('500x300')
#     root.configure(bg='#2d2d2d')

#     frame = Frame(root, bg='white', bd=5)  
#     frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#     Label(frame, text="Your ICT-U Email", bg='white', fg='black', font=('Arial', 20)).pack(pady=10)  # Set background color to white and foreground color to black
#     email_entry = Entry(frame, bg='#5F5F5F', fg='white', font=('Arial', 20))
#     email_entry.pack(ipady=10)

#     login_button = Button(frame, text="Login", bg='black', fg='white', font=('Arial', 20), command=lambda: token_page(root))
#     login_button.pack(pady=20)

# def token_page(root):
#     for widget in root.winfo_children():
#         widget.destroy()

#     root.title("Token Verification")
#     root.geometry('500x300')
#     root.configure(bg='#2d2d2d')

#     frame = Frame(root, bg='white', bd=5)  # Set background color to white
#     frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#     Label(frame, text="Enter Token", bg='white', fg='black', font=('Arial', 20)).pack(pady=10)  # Set background color to white and foreground color to black
#     token_entry = Entry(frame, bg='#5F5F5F', fg='white', font=('Arial', 20))
#     token_entry.pack(ipady=10)

#     submit_button = Button(frame, text="Submit", bg='black', fg='white', font=('Arial', 20), command=lambda: dashboard_page(root))
#     submit_button.pack(pady=20)

#     reenter_button = Button(frame, text="Did not receive token, re-enter email", bg='black', fg='white', font=('Arial', 20), command=lambda: login_page(root))
#     reenter_button.pack(pady=20)

# root = Tk()
# login_page(root)
# root.mainloop()