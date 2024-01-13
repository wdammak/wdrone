# wdrone/scripts/planning_interface.py

from flask import Flask, render_template, request, jsonify
import threading
import sqlite3

app = Flask(__name__)
DB_PATH = 'wdrone/tasks.db'

def init_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)''')
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT task FROM tasks')
    tasks = [row[0] for row in cursor.fetchall()]
    conn.close()
    return tasks

def add_task(task):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (task) VALUES (?)', (task,))
    conn.commit()
    conn.close()

def remove_task(task):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE task=?', (task,))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    tasks = get_tasks()
    return render_template('planning.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task_route():
    new_task = request.form['task']
    add_task(new_task)
    return jsonify({"success": True, "tasks": get_tasks()})

@app.route('/remove_task', methods=['POST'])
def remove_task_route():
    task_to_remove = request.form['task']
    remove_task(task_to_remove)
    return jsonify({"success": True, "tasks": get_tasks()})

def run_app():
    init_database()
    app.run(debug=True, use_reloader=False, port=5002)

if __name__ == '__main__':
    threading.Thread(target=run_app).start()
