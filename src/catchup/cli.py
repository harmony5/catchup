import typer


cli = typer.Typer()


@cli.command()
def add(todo: str):
    typer.echo(f"Added {todo} to todos.txt")


@cli.command()
def remove(todo: str):
    typer.echo(f"Removed {todo} from todos.txt")


if __name__ == "__main__":
    cli()
