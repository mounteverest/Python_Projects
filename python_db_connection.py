__author__ = 'kalyani'
# import sqlite3 libray
import sqlite3

# make a database connection in sqlite
conn = sqlite3.connect("new.db")
# cursor is used to execute the sql commands and sql query
cursor = conn.cursor()
# create a table
cursor.execute("""CREATE TABLE Employee
                (Emp_id INT, Title TEXT, Salary INT)
               """)
# close the connection
conn.close()
