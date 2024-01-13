# wdrone/scripts/center_control_app.py

from flask import Flask, render_template, request, jsonify
import threading
import time

app = Flask(__name__)
task_info = {"current_task": None, "remaining_tasks": []}
lock = threading.Lock()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_info', methods=['POST'])
def update_info():
    global task_info
    with lock:
        task_info = request.get_json()
    return jsonify({"success": True})

@app.route('/get_info', methods=['GET'])
def get_info():
    global task_info
    with lock:
        return jsonify(task_info)

def run_app():
    app.run(debug=True, use_reloader=False, port=5001)

if __name__ == '__main__':
    threading.Thread(target=run_app).start()

# Reste du script...
