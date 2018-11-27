import sqlite3 as sql
connection = sql.connect("sathya.db")
print(connection)
print(type(connection))