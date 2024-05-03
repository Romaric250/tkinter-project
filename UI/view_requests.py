from tkinter import *

def view_request_status_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Request Status")
    root.geometry('500x300')
    root.configure(bg='#2d2d2d')

    frame = Frame(root, bg='white', bd=5)  # Set background color to white
    frame.place(relx=0.5, rely=0.5, relwidth=0.9, anchor=CENTER)  # Adjust relwidth to 0.9

    Label(frame, text="Request Status", bg='white', fg='black', font=('Arial', 20), wraplength=450).pack(pady=10)

    sample_data = [
        {"request": "Request 1", "status": "Pending"},
        {"request": "Request 2", "status": "Approved"},
        {"request": "Request 3", "status": "Rejected"},
    ]

    for i, data in enumerate(sample_data):
        request_frame = Frame(frame, bg='lightgrey', bd=5)
        request_frame.pack(pady=10)
        Label(request_frame, text=f"{data['request']} - {data['status']}", bg='lightgrey', fg='black', font=('Arial', 20)).pack()

    back_button = Button(frame, text="Back", bg='black', fg='white', font=('Arial', 20), command=lambda: go_back(root))
    back_button.pack(pady=20)

def go_back(root):
    from UI.dashboard import dashboard_page
    dashboard_page(root)
    
    