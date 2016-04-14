__author__ = 'kalyani'

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    car_inventory = [
        ('Hundae', 'Ivory', 2012),
        ('Ford', 'Red', 2016)
        ]
    c.executemany('INSERT INTO car_type VALUES (? ,? ,?)', car_inventory)


