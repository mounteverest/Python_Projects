
__author__ = 'kalyani'

import sqlite3

# make a database connection to sqlite3
conn = sqlite3.connect("cars.db")

# Execute the sql query
cursor = conn.cursor()

# make a table
cursor.execute(""" CREATE TABLE car_type
                (car_make TEXT, car_color TEXT,car_year INT)
               """)

# cursor.execute("INSERT INTO cars VALUES('Honda', 'Blue',1997)")
#
# cursor.execute("INSERT INTO cars VALUES('BMW', 'Black', 2004)")

conn.close()
