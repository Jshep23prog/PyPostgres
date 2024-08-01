from tkinter import *
from tkinter import ttk
import os
import psycopg2

from dotenv import load_dotenv
load_dotenv()
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

root = Tk()
root.title("Student DBMS")
#create a frame for window
frame = LabelFrame(root, text = "Student Data")
frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
#put labels on the frame instead of the window
Label(frame, text="Name:").grid(row=0, column=0, padx=2, sticky="w")
name_entry = Entry(frame)
name_entry.grid(row=0, column=1, pady=2, sticky="ew")

Label(frame, text="Address:").grid(row=1, column=0, padx=2, sticky="w")
address_entry = Entry(frame)
address_entry.grid(row=1, column=1, pady=2, sticky="ew")

Label(frame, text="Age:").grid(row=2, column=0, padx=2, sticky="w")
age_entry = Entry(frame)
age_entry.grid(row=2, column=1, pady=2, sticky="ew")

Label(frame, text="Phone Number:").grid(row=3, column=0, padx=2, sticky="w")
phone_entry = Entry(frame)
phone_entry.grid(row=3, column=1, pady=2, sticky="ew")

#create a button frame

button_frame = Frame(root)
button_frame.grid(row=1, column=0, pady=5, sticky="ew")

Button(button_frame, text="Create Table").grid(row=0, column=0, padx=5)
Button(button_frame, text="Add Data").grid(row=0, column=1, padx=5)
Button(button_frame, text="Update Data").grid(row=0, column=2, padx=5)
Button(button_frame, text="Delete Data").grid(row=0, column=3, padx=5)

#create frame for the data tree
tree_frame = Frame(root)
tree_frame.grid(row=2, column=0, padx=10, sticky="nsew")

tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="browse") #attach scrollbar to treeview
tree.pack()
tree_scroll.config(command=tree.yview)




root.mainloop()