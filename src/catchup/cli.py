"""CLI tool to manage your to-do's.
"""

from os import write
import typer
import csv


cli = typer.Typer()


@cli.command()
def add(todo: str):
    """Add new to-do.
    """
    with open("todos.txt", "a") as todo_file:
        id = str(abs(hash(todo)))[:5]
        writer = csv.writer(todo_file, "unix")
        writer.writerow([id, todo, "In Progress"])

    typer.echo(f"Added {todo} to todos.txt:")
    with open("todos.txt") as todo_file:
        todos = csv.reader(todo_file, "unix")
        for id, desc, status in todos:
            typer.echo(f"{id:6}\t{desc}\t{status}")


@cli.command()
def complete(todo: str):
    """Mark a specific to-do as completed.
    """
    typer.echo(f"Todo [{todo}] was marked as completed.")


@cli.command()
def remove(todo: str):
    """Remove a specific to-do from the list.
    """
    typer.echo(f"Removed [{todo}] from todos.txt")


if __name__ == "__main__":
    cli()
