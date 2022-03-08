import sqlite3 as sql
connection = sql.connect("college.db")
connection.execute('''create table student(
id integer primary key autoincrement,
NAME text,
ROLLNUMBER integer,
ADMINNO integer,
COLLEGE text);
''')
print("table created succesfully")
getname = input("enter the name:")
getrollnum = input("enter roll number:")
getAdmin = input("enter admno number:")
getCollegeName = input("enter college name:")
connection.execute("insert into student(NAME,ROLLNUMBER,ADMINNO,COLLEGE) \
                   values('"+getname+"',"+getrollnum+","+getAdmin+",'"+getCollegeName+"')")
connection.commit()
connection.close()
print("Inserted Succesfully")