__author__ = 'kalyani'


import csv

import sqlite3

with sqlite3.connect("student_contact.db") as connection:
    c = connection.cursor()

    students = csv.reader(open("students.csv", "rU"))

    c.execute("CREATE TABLE students(first_name TEXT, last_name TEXT)")
    c.executemany("INSERT INTO students(first_name,last_name)values (? , ?)", students)