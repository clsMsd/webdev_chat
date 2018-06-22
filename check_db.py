import sqlite3

con = sqlite3.connect("webchat.db")

result = con.execute("select * from Content").fetchall()

print(result)
print(result[1][1])

con.close()