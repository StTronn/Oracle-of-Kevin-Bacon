##remove overlaping in movies and actors key 
import sqlite3

conn= sqlite3.connect("movies.db")
cur=conn.cursor();
cur.execute("SELECT * from stars")
stars=cur.fetchall()
for star in stars:
    movie_id="mv"+str(star[0])  
    person_id="p"+str(star[1])
    cur.execute("INSERT INTO stars_new VALUES(?,?)",(movie_id,person_id))

# cur.execute("SELECT * FROM movies")
# movies=cur.fetchall()
# for movie in movies:
#     id="mv"+str(movie[0]);
#     title=movie[1];
#     year=movie[2]
#     cur.execute("INSERT INTO movies_new VALUES(?,?,?)",(id,title,year))


conn.commit()
conn.close()