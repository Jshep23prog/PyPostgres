import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

def create_table():
    conn = psycopg2.connect(dbname="pydb", user=db_user, password=db_password)
    cur = conn.cursor()
    cur.execute("create table students(student_id serial primary key,name text,address text,age int,number text);")
    print("Student table created")
    conn.commit()
    conn.close

def insert_data():
    #code to accept data from the user
    name = input("Enter name: ")
    address = input("Enter address: ")
    age = input("Enter age: ")
    number = input("Enter number: ")
    conn = psycopg2.connect(dbname="pydb", user=db_user, password=db_password)
    cur = conn.cursor()
    cur.execute("insert into students(name, address, age, number) values(%s, %s, %s, %s)", (name, address, age, number))
    print("Data added in student table")
    conn.commit()
    conn.close

def update_data():
    student_id = input("Enter id of the student to be updated")
    name = input("Enter name: ")
    address = input("Enter address: ")
    age = input("Enter age: ")
    number = input("Enter number: ")
    conn = psycopg2.connect(dbname="pydb", user=db_user, password=db_password)
    cur = conn.cursor()
    cur.execute("update students set name=%s , address=%s , age=%s, number=%s where student_id=%s", (name, address, age, number, student_id))
    conn.commit()
    conn.close()

# insert_data
update_data()