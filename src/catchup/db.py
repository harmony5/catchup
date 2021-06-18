from typing import Iterator, Any, Mapping
import dataset
from datetime import datetime


DB: dataset.Database = dataset.connect("sqlite:///todos.db")

TODOS: dataset.Table = DB.create_table("todos", primary_id="id")
TODOS.create_column("description", DB.types.text)
TODOS.create_column("status", DB.types.string(12))
# .create_column("timestamp", DB.types.datetime, nullable=False, default=now())


def get_todos() -> Iterator[Mapping[str, Any]]:
    global TODOS
    return TODOS.all()


def get_todo(todo_id: int) -> Mapping[str, Any]:
    global TODOS
    return TODOS.find_one(id=todo_id)


def get_todos_by_status(status: str) -> Iterator[Mapping[str, Any]]:
    global TODOS
    return TODOS.find(status=status)


def add_todo(description: str):
    global TODOS

    TODOS.insert(
        {
            "description": description,
            "status": "In Progress",
            "timestamp": datetime.now(),
        }
    )


def update_todo(todo_id: int, **fields):
    global TODOS

    fields.update({"id": todo_id})

    # Update fields in all rows with matching id's.
    TODOS.update(row=fields, keys=["id"])


def delete_todo(todo_id: int):
    global TODOS
    TODOS.delete(id=todo_id)
