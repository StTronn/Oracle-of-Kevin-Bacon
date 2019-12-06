import sqlite3

conn=sqlite3.connect("movies.db")
cur=conn.cursor()

cur.execute("SELECT * FROM stars_new")
edges=cur.fetchall()
for edge in edges:
    cur.execute("INSERT INTO edges VALUES(?,?)",(edge[0],edge[1]))
    cur.execute("INSERT INTO edges VALUES(?,?)",(edge[1],edge[0]))
    
conn.commit()
conn.close()