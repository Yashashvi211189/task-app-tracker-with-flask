from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/tasks')
def view_tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task')
    if task_name:
        new_task = Task(name=task_name)
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('view_tasks'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('view_tasks'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/check-status')
def check_status():
    return jsonify({'status': 'running', 'database': 'connected'})

def create_app():
    with app.app_context():
        db.create_all()
    return app

if __name__ == '__main__':
    os.makedirs('instance', exist_ok=True)
    app = create_app()
    app.run(host='0.0.0.0', port=8000, debug=True)