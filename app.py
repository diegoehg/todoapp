from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://todoapp:todo_user@localhost:5432/todoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Todo id:{self.id}, description:{self.description}>"


db.create_all()


@app.route("/")
def index():
    todos = [
            {'description': 'Task 1'},
            {'description': 'Task 1'},
            {'description': 'Task 1'}
    ]

    return render_template('index.html', data=todos)


if __name__ == '__main__':
    app.run()
