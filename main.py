from tkinter import *
from tkinter import ttk
import chat

def main_page(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Welcome Page")
    root.geometry('300x200')

    frame = ttk.Frame(root, padding="10")
    frame.pack(fill=BOTH, expand=True)

    ttk.Label(frame, text="Welcome!").grid(row=0, column=0, sticky=W)

    chat_button = ttk.Button(frame, text="Go to Chat", command=lambda: chat.chat_page(root))
    chat_button.grid(row=1, column=0)

    frame.columnconfigure(0, weight=1)