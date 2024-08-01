from tkinter import *
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

root.mainloop()