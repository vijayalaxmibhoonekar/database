import sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
try:
    curs.execute("insert into Employee values(101,'Ravi',12500.0)")
    conn.commit()
    print("101 Employee Inserted")
except sql.IntegrityError as ie:
    print("idno is available")
finally:
    curs.close()
    conn.close()
print("thanks")