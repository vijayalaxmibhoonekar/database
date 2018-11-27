import sqlite3 as sql
conn=sql.connect("sathya.db")
curs=conn.cursor()
curs.execute("create table Employee(idno number,name text,salary real)")
print("table created")
curs.close()
conn.close()
print("thanks")