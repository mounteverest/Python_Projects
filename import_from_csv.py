__author__ = 'kalyani'
# import from CSV
# import the csv library
# import csv
#
# import sqlite3
#
# with sqlite3.connect("new1.db") as connection:
#     c = connection.cursor()
#
# # open the csv file and assign it to a variable
#     employees = csv.reader(open("employees.csv", "rU"))
#
# # create a new table called employees
#     c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")
#
# # insert data into table
#     c.executemany("INSERT INTO employees(firstname, lastname)values (?, ?)", employees)



import csv

import sqlite3

with sqlite3.connect("empl.db") as connection:
    c = connection.cursor()

    employees = csv.reader(open("employees.csv", "rU"))

    c.execute("CREATE TABLE employees(first_name TEXT, last_name TEXT)")

    c.executemany("INSERT INTO employees(first_name,last_name)values (? , ?)", employees)

