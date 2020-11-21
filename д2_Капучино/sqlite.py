from sqlite3 import connect

con = connect('coffee.db')
cur = con.cursor()