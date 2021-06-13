import dataset
from datetime import datetime


DB = dataset.connect("sqlite:///../../todos.db")
TODOS = DB["todos"]


def add_todo(id: int, description: str):
    global TODOS

    TODOS.insert(
        {
            "id": id,
            "description": description,
            "status": "In Progress",
            "creation_date": str(datetime.now()),
        }
    )


def get_todos():
    global TODOS
    return TODOS.all()


def get_todo(id: int):
    global TODOS
    return TODOS.find_one(id=id)


def get_todos_by_status(status: str):
    global TODOS
    return TODOS.find(status=status)
