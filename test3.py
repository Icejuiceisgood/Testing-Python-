import sqlite3

conn = sqlite3.connect('/Users/risha/databases/test.db')
cur = conn.cursor()
cur.execute("Create table if not exists Room ('id' Integer Primary Key, 'building' varchar(200), 'number' varchar(200))")
conn.commit()
cur.execute("Select * from student")
print(cur.fetchall())
cur.execute("Select * from student")
for row in cur:
    print(row)
cur.execute("Insert or ignore into student (id,name,birthday) values (?,?,?)", (3,"Jake","10/07/02"))
conn.commit()
cur.close()






