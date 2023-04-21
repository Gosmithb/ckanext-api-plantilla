import click


@click.group(short_help="api_plantilla CLI.")
def api_plantilla():
    """api_plantilla CLI.
    """
    pass


@api_plantilla.command()
@click.argument("name", default="api_plantilla")
def command(name):
    """Docs.
    """
    click.echo("Hello, {name}!".format(name=name))


def get_commands():
    return [api_plantilla]
