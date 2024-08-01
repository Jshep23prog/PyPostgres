import psycopg2

def create_table():
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
    cur = conn.cursor()
    cur.execute("insert into students(name, address, age, number) values(%s, %s, %s, %s)", (name, address, age, number))
    print("Data added in student table")
    conn.commit()
    conn.close

insert_data()