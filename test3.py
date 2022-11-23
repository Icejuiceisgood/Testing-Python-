import sqlite3

conn = sqlite3.connect('/Users/risha/databases/test.db')
cur = conn.cursor()
cur.execute("Select * from student")
cur.execute("Insert or ignore into student (id,name,birthday) values (?,?,?)", (3,"Jake","10/07/02"))
cur.close()






