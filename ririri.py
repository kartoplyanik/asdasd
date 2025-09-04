import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

if__name__ == '__main__':
    app.run(debug=True)
#conn = sqlite3.connect('baza.db')
#cursor = conn.cursor()
#login = input("Введіть логін")
#cursor.execute(f"SELECT name FROM users WHERE name=='{login}'")
#data = cursor.fetchall()
#print("ваші логіни співпадають")
