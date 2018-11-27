import  sqlite3 as sql
conn = sql.connect("sathya.db")
curs = conn.cursor()
curs.execute("select*from Employee")
res = curs.fetchall()
for x in res:
    idno,name,salary=x
    print(idno,"==",name,"===",salary)