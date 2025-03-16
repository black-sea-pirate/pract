from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

tasks = []
@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    if title:
        task = {'title': title, 'completed': False}
        tasks.append(task)
    return redirect(url_for('index'))


@app.route('/complete/<int:task_index>', methods=['GET'])
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:task_index>', methods = ['GET'])
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
