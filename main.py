from bottle import route, run, template, redirect, request
import sqlite3

con = sqlite3.connect("webchat.db")

@route("/", method="GET")
def home():
    sql = f"SELECT * FROM Content"
    result = con.execute(sql)
    return template("home", content=result.fetchall())

@route("/", method="POST")
def home():
    name = request.forms.name
    message = request.forms.message
    print(name, message)

    sql = f"INSERT INTO Content (name, message) VALUES('{name}', '{message}')"
    con.execute(sql)
    con.commit()
    
    redirect("/")

if __name__ == "__main__":
    run(host="0.0.0.0", port=8080, debug=True, reloader=True)
