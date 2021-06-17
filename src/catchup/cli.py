"""CLI tool to manage your to-do's.
"""

from typing import Optional
import typer
from tabulate import tabulate as tab
import src.catchup.db as db
from src.catchup import __version__


cli = typer.Typer(help=__doc__)


STATE = {"verbose": False}
VALID_STATUSES = [
    ('"in progress"', "shows only to-do's in progress."),
    ("completed", "shows only completed to-do's."),
]


def version_callback(value: bool):
    if value:
        typer.echo(f"catchup v{__version__}")
        raise typer.Exit()


def status_callback(status: Optional[str]):
    if status is not None and status.lower() not in ("in progress", "completed"):
        raise typer.BadParameter(
            "Status '{status}' not recognized. Must be one of 'in progress' or 'completed'."
        )
    return status


def status_completion(incomplete: str):
    for status, help_msg in VALID_STATUSES:
        if status.startswith(incomplete):
            yield (status, help_msg)


@cli.callback()
def main(
    verbose: bool = False,
    version: bool = typer.Option(None, "--version", "-v", callback=version_callback),
):
    if verbose:
        STATE["verbose"] = True
        typer.echo("Verbose mode on.")


@cli.command()
def show(
    status: Optional[str] = typer.Option(
        None,
        "--status",
        "-s",
        help="List only the to-do's with specified status.",
        callback=status_callback,
        autocompletion=status_completion,
    )
):
    """Show saved to-do's.
    """
    if status:
        todos = db.get_todos_by_status(status.title())
    else:
        todos = db.get_todos()
    typer.echo(tab(todos, headers="keys"))


@cli.command()
def add(todo: str):
    """Add new to-do with TODO as the description.
    """
    db.add_todo(todo)

    typer.echo(f"Saved new to-do to the Database: {todo}")

    if STATE["verbose"]:
        typer.echo(tab(db.get_todos_by_status("In Progress"), headers="keys"))


@cli.command()
def complete(todo_id: int):
    """Mark the to-do specified by TODO_ID as completed.
    """
    db.update_todo(todo_id, status="Completed")
    typer.echo(f"Todo with id #{todo_id} was marked as completed.")


@cli.command()
def remove(todo_id: int):
    """Remove the to-do specified by TODO_ID from the list.
    """
    db.delete_todo(todo_id)
    typer.echo(f"Removed to-do with id #{todo_id}.")


if __name__ == "__main__":
    cli()
