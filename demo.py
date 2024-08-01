#import dependencies os for dotenv support, psycopg2 to communicate with postgresdb
import os
import psycopg2

from dotenv import load_dotenv
load_dotenv()
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
#function to create a table
def create_table():
    conn = psycopg2.connect(dbname="pydb", user=db_user, password=db_password) #assign to variable conn for connection using dotenv vars to keep info safe from internet
    cur = conn.cursor()
    cur.execute("create table students(student_id serial primary key,name text,address text,age int,number text);") #create the table and row 'schema'
    print("Student table created")
    conn.commit() #save changes
    conn.close #close connection

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

#add a delete function
def delete_data():
    student_id = input("Enter the ID of the student you want to delete: ")
    conn = psycopg2.connect(dbname="pydb", user=db_user, password=db_password)
    cur = conn.cursor()
    #determine if student exists
    cur.execute("select * from students where student_id=%s", (student_id, ))
    student = cur.fetchone()

    if student:
      print(f"Student to be deleted: ID {student[0]}, Name: {student[1]}, Address: {student[2]}, Number {student[3]}")
      choice = input("Are you sure you want to delete your student? (yes/no)")
      if choice.lower() == "yes":
          cur.execute("delete from students where student_id=%s", (student_id, ))
          print("Student record deleted")
      else:
          print("Deletion cancelled")
    else:
        print("Student not found")
    conn.commit()
    conn.close()

def update_data():
    student_id = input("Enter id of the student to be updated")
    conn = psycopg2.connect(dbname="pydb", user=db_user, password=db_password)
    cur = conn.cursor()
    fields = {          #only update specific fields with this dictionary object
        "1":("name", "Enter the new name"), #tuple with name update option and message to the user
        "2":("address", "Enter the new address"),
        "3":("age", "Enter the new age"),
        "4":("number", "Enter the new number"),
    }
    print("Which field would you like to update?")
    #loop through fields
    for key in fields:
        print(f"{key}:{fields[key][0]}")
    field_choice = input("Enter the number of the field you want to update: ")
    #logic for if choice is present in field
    if field_choice in fields:
        field_name, prompt = fields[field_choice]
        new_value = input(prompt)
        #make query dynamic
        sql = f"update students set {field_name}= %s where student_id=%s" #moved tuple values to execute line as f string is only string not arguments also
        cur.execute(sql, (new_value, student_id))
        print(f"{field_name} updated successfully")
    else:
        print("Invalid choice")


    conn.commit()
    conn.close()

# insert_data
# update_data()
delete_data()