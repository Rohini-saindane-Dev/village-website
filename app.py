import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Database create function
def init_db():
    conn = sqlite3.connect('village.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Home page
@app.route('/')
def home():
    conn = sqlite3.connect('village.db')
    cursor = conn.cursor()
    cursor.execute("SELECT message FROM notices")
    notices = cursor.fetchall()
    conn.close()

    return render_template('index.html', notices=notices)

# Add notice
@app.route('/add_notice', methods=['POST'])
def add_notice():
    message = request.form['message']

    conn = sqlite3.connect('village.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notices (message) VALUES (?)", (message,))
    conn.commit()
    conn.close()

    return "Notice Added Successfully!"

# Agriculture page
@app.route('/agriculture')
def agriculture():
    return render_template('agriculture.html')

# School page
@app.route('/school')
def school():
    return render_template('school.html')

# Temples page
@app.route('/Temples')
def temples():
    return render_template("temples.html")

# Culture page
@app.route("/culture")
def culture():
    return render_template("culture.html")

# Contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")

# About page
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/nature')
def nature():
    return render_template('nature.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)