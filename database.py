import pymysql
from tkinter import messagebox

def connect_database():
    
    try:
        conn=pymysql.connect(host='localhost',user='root',password='1234')
        mycursor=conn.cursor()

    except:
        messagebox.showerror('error','something went wrong')
        return
    
    mycursor.execute('CREATE DATABASE employee_data')
    mycursor.execute('USE employee_data')
    mycursor.execute('CREATE TABLE data(Id VARCHAR(30),Name VARCHAR(50),Phone VARCHAR(15),Role VARCHAR(50),Gender VARCHAR(20),Salary DECIMAL(10,2))')


def insert(id,name,phone,role,gender,salary):
  print(id,name,phone,role,gender,salary)
    #mycursor.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))
    #conn.commit()

connect_database()