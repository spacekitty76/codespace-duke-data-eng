#!/usr/bin/env python
"""Super simple app to setup containerization of a cli tool."""
import click


@click.command()
@click.option("--name")
def hello(name):
    click.echo(f"Hello {name}!")


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    hello()
