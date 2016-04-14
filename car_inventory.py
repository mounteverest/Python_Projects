__author__ = 'kalyani'

import sqlite3
# Using with to save data automatically without using commit

with sqlite3.connect("cars.db") as connection:

    c = connection.cursor()

    c.execute("INSERT INTO car_type VALUES ('Toyaota', 'Green', 1998)")
    c.execute("INSERT INTO car_type VALUES('Audi','White', 2007)")
