import dataset
from datetime import datetime


DB = dataset.connect("sqlite:///todos.db")
TODOS = DB["todos"]


def get_todos():
    global TODOS
    return TODOS.all()


def get_todo(todo_id: int):
    global TODOS
    return TODOS.find_one(id=todo_id)


def get_todos_by_status(status: str):
    global TODOS
    return TODOS.find(status=status)


def add_todo(description: str):
    global TODOS

    TODOS.insert(
        {
            # "id": str(hash(description))[:6],
            "description": description,
            "status": "In Progress",
            # "creation_date": str(datetime.now()),
        }
    )


def update_todo(todo_id: int, **fields):
    global TODOS

    data = fields.update({"id": todo_id})

    # Update fields in all rows with matching id's.
    TODOS.update(row=data, keys=["id"])


def delete_todo(todo_id: int):
    global TODOS
    TODOS.delete(id=todo_id)
