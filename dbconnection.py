import sqlite3

def getConnection():
    conn = sqlite3.connect("todo.db")
    return conn

def save_work(work):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS todolist (id INTEGER PRIMARY KEY AUTOINCREMENT, work TEXT)")
    cursor.execute("INSERT INTO todolist (work) VALUES (?)",(work,))
    conn.commit()
    conn.close()

def view_data():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todolist")
    data = cursor.fetchall()
    conn.close()
    return data 

def delete_data(id):
    conn = getConnection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM todolist WHERE id=?", (id,))
    conn.commit()
    conn.close()

