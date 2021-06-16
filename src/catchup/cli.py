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
    db.add_todo(todo)

    typer.echo(f"Saved new to-do to the Database: {todo}")
    typer.echo(tab(db.get_todos_by_status("In Progress"), headers="keys"))


@cli.command()
def complete(todo_id: int):
    """Mark the to-do specified by <todo_id> as completed.
    """
    db.update_todo(todo_id, status='Completed')
    typer.echo(
        f"Todo with id #{todo_id} was marked as completed."
    )


@cli.command()
def remove(todo_id: int):
    """Remove the to-do specified by <todo_id> from the list.
    """
    todo = db.get_todo(todo_id)
    db.delete_todo(todo_id)
    typer.echo(f"Removed to-do with id #{todo_id}: {todo['description']}")


if __name__ == "__main__":
    cli()
