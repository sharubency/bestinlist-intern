#1. Create a connection for DB and print the version using a python program
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shee@123"
)
print(mydb)

cur = mydb.cursor()
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print("DBMS Version :",str(data))

#2. Create a multiple tables & insert data in table

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shee@123",
  database="mydatabase"


)

dbse = mydb.cursor()
dbse.execute("CREATE TABLE Office (emp_name VARCHAR(255), Employee_id VARCHAR(255) ,EMP_ADDRESS VARCHAR(255))")
dbse = mydb.cursor()
dbse.execute("CREATE TABLE Student(rollno INT(24) , STUD_NAME VARCHAR(255) , MARK INT(3))")


dbse = mydb.cursor()
dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)
dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)


#3. Create a employee table and read all the employee name in the table using for loop

import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shee@123",
  database="mydatabase"


)
mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"
val = ("138","Keran","Nungambakkam")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"
val = ("132","harish","T Nagar")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"
val = ("135","Iniya","Thambaram")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

#------------------------------------------or---------------------------------------------


import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",
  password="Shee@123",
  database="mydatabase"


)
mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"
val = [
  ('1','Geetha Kumar', 'pb 4'),
  ('2','Rufeena Fernandes', 'ph 652'),
  ('3','Anjali Dhas', '13ry 21'),
  ('4','Sanjay Anto', 'bb 345'),
  ('5','Maria', 'pfb 2'),
  ('6','Vignesh', 'vik 1633')
]

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "was inserted.")

#------------------------------print using for loop--------------------------

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Employee1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#----------------------------------print specific column-----------------------------------

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM Employee1")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


