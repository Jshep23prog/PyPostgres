import psycopg2

conn = psycopg2.connect()
cur = conn.cursor()
cur.execute("create table students(student_id serial primary key,name text,address text,age int,number text);")
print("Student table created")
conn.commit()
conn.close