from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)


tasks = []

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task_text = request.form.get("task")
    print(task_text)
    if task_text:
        task = {
            'id': len(tasks) + 1,
            'text': task_text,
            'created_at': datetime.now(),
            'completed': False
        }
        tasks.append(task)
    return redirect(url_for("index"))

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            break
    return redirect(url_for("index"))

if __name__ == "__main__":
    print("запуск")
    app.run(debug=True)