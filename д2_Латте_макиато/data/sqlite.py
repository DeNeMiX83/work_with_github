from sqlite3 import connect

con = connect('data/coffee.db')
cur = con.cursor()