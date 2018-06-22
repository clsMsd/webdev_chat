import sqlite3

con = sqlite3.connect("webchat.db")

con.execute("""
CREATE TABLE Content (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    message TEXT NOT NULL
)
""")
con.commit()

con.execute("INSERT INTO Content (name, message) VALUES('管理者', 'テスト投稿')")
con.commit()

con.close()
