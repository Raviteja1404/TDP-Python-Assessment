import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Raviteja@1404",
    database="studentDetails"
    )
mycursor=mydb.cursor()
mycursor.execute("create table students(student_id INT AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(255),last_name VARCHAR(255),age INT, grade FLOAT)")
task="insert into students(first_name,last_name,age,grade) values(%s,%s,%s,%s)"
val=("Alice","Smith",18,95.5)
mycursor.execute(task,val)

task="update students set grade =97.0 where first_name='Alice'"
mycursor.execute(task)

task="delete from students where last_name='Smith'"
mycursor.execute(task)

task="select * from students"
mycursor.execute(task)
myres=mycursor.fetchall()
for x in myres:
    print(x)
