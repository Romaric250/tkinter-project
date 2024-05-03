from tkinter import *
from tkinter import ttk

def chat_page(root):
    root.title("Chat Page")
    root.geometry('500x500')

    frame = ttk.Frame(root, padding="10")
    frame.pack(fill=BOTH, expand=True)

    chat_text = Text(frame)
    chat_text.grid(row=0, column=0, columnspan=2, sticky=(W, E, N, S))

    message_entry = ttk.Entry(frame)
    message_entry.grid(row=1, column=0, sticky=(W, E))

    send_button = ttk.Button(frame, text="Send")
    send_button.grid(row=1, column=1)

    frame.columnconfigure(0, weight=1)
    frame.rowconfigure(0, weight=1)