from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/move/<int:task_id>/<direction>')
def move_task(task_id, direction):
    if direction == 'up' and task_id > 0:
        tasks[task_id], tasks[task_id - 1] = tasks[task_id - 1], tasks[task_id]
    elif direction == 'down' and task_id < len(tasks) - 1:
        tasks[task_id], tasks[task_id + 1] = tasks[task_id + 1], tasks[task_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
