__author__ = 'kalyani'

# import sqlite3 library
import sqlite3

# make database in sqlite3
conn = sqlite3.connect("cars.db")

# Execute the sql query
cursor = conn.cursor()

# Insert Data into Tables
cursor.execute("INSERT INTO car_type VALUES ('Honda','Black',1997)")

cursor.execute("INSERT INTO car_type VALUES ('BMW', 'Blue',2001)")
# To store the data
conn.commit()
# Close the Table
conn.close()