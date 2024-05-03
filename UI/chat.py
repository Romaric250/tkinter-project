import requests
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

def chat_page(root):
    root.title("Chat Page")
    root.geometry('500x500')

    frame = ttk.Frame(root, padding="10")
    frame.pack(fill=BOTH, expand=True)
    
    name_label = ttk.Label(frame, text="Name:")
    name_label.grid(row=0, column=0, sticky=W)
    name_entry = ttk.Entry(frame, width=30)
    name_entry.grid(row=0, column=1, sticky=(W, E))

    age_label = ttk.Label(frame, text="Age:")
    age_label.grid(row=1, column=0, sticky=W)
    age_entry = ttk.Entry(frame, width=30)
    age_entry.grid(row=1, column=1, sticky=(W, E))

    level_label = ttk.Label(frame, text="Level:")
    level_label.grid(row=2, column=0, sticky=W)
    level_entry = ttk.Entry(frame, width=30)
    level_entry.grid(row=2, column=1, sticky=(W, E))

    topic_label = ttk.Label(frame, text="Request Topic:")
    topic_label.grid(row=3, column=0, sticky=W)
    topic_entry = ttk.Entry(frame, width=30)
    topic_entry.grid(row=3, column=1, sticky=(W, E))

    message_label = ttk.Label(frame, text="Message:")
    message_label.grid(row=4, column=0, sticky=W)
    message_entry = Text(frame, height=5, width=30)
    message_entry.grid(row=4, column=1, sticky=(W, E))

    attachment_button = ttk.Button(frame, text="Add Attachment", command=lambda: filedialog.askopenfilename())
    attachment_button.grid(row=5, column=0, sticky=W)

    def submit_request():
        if not name_entry.get() or not age_entry.get() or not level_entry.get() or not topic_entry.get() or not message_entry.get("1.0", "end").strip():
            messagebox.showerror("Error", "All fields are required except attachment.")
        else:
            
            url = "http://127.0.0.1:5000/create_request/6634c36b260690dbf1796828"

           
            data = {
                "name": name_entry.get(),
                "age": age_entry.get(),
                "level": level_entry.get(),
                "topic": topic_entry.get(),
                "message": message_entry.get("1.0", "end").strip()
            }

            
            response = requests.post(url, json=data)

           
            if response.status_code == 200:
                messagebox.showinfo("Success", "Request successfully submitted.")
                go_back(root)
            else:
                messagebox.showerror("Error", "Failed to submit request.")

    def go_back(root):
        from dashboard import dashboard_page
        dashboard_page(root)

    submit_button = ttk.Button(frame, text="Submit Request", command=submit_request)
    submit_button.grid(row=5, column=1, sticky=E)

    frame.columnconfigure(1, weight=1)