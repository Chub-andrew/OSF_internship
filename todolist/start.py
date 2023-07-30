from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:password@localhost:5432/to_do_db'
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/", methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route('/main', methods=['GET'])
def main():
    tasks = Task.query.all()
    return render_template('main.html', tasks=tasks)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    #jsonify
    tasks_json = jsonify([{
        "id": task.id,
        "title": task.title,
        "description": task.description
    } for task in tasks])
    return tasks_json

@app.route("/task/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        print("abort(404)")
    return jsonify(task.to_json())


@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form['description']

    db.session.add(Task(title=title, description=description))
    db.session.commit()
    return redirect(url_for('main'))


@app.route("/update_task/<int:task_id>", methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)

    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    db.session.commit()
    return jsonify(task.to_json())

    #
    # if request.method == 'POST':
    #     title = request.form['title']
    #     description = request.form['description']
    #
    #     task.title = title
    #     task.description = description
    #
    #     db.session.commit()
    #     return redirect(url_for('main'))

    # return render_template('update_task.html', task=task)

@app.route("/delete_task/<int:task_id>", methods=['GET', 'POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)

    if task is None:
        print("abort(404)")
    db.session.delete(task)
    db.session.commit()
    return jsonify({'result': True})

    # if request.method == 'POST':
    #     db.session.delete(task)
    #     db.session.commit()
    #     return redirect(url_for('main'))
    #
    # return render_template('delete_task.html', task=task)

if __name__ == '__main__':
    app.run(debug=True)
