from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

tasks = []

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/print')
def print_tasks():
    return "<br>".join(tasks)

if __name__ == '__main__':
    app.run(debug=True)
