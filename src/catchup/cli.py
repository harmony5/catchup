"""CLI tool to manage your to-do's.
"""

import typer
from tabulate import tabulate as tab
import catchup.db as db


cli = typer.Typer()


@cli.command()
def show():
    """Show all to-do's.
    """
    todos = list(db.get_todos())
    typer.echo(tab(todos, headers="keys"))


@cli.command()
def add(todo: str):
    """Add new to-do.
    """
    todo_id = str(hash(todo))[:6]
    db.add_todo(todo_id, todo)

    typer.echo(f"Added {todo} to todos.txt:")

    typer.echo("Id\tDescription\tStatus\tCreated At")
    for todo in db.get_todos_by_status("In Progress"):
        typer.echo(
            f"{todo['id']}\t"
            f"{todo['description']}\t"
            f"{todo['status']}\t"
            f"{todo['creation_date']}"
        )


@cli.command()
def complete(todo_id: int):
    """Mark the to-do specified by <todo_id> as completed.
    """
    todo = db.get_todo(todo_id)
    typer.echo(
        f"Todo with id #{todo_id} {todo['description']} was marked as completed."
    )


@cli.command()
def remove(todo_id: int):
    """Remove the to-do specified by <todo_id> from the list.
    """
    todo = db.get_todo(todo_id)
    typer.echo(f"Removed to-do with id #{todo_id}: {todo['description']}.")


if __name__ == "__main__":
    cli()
