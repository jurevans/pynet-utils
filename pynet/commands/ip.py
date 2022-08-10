import click
from pynet.lib.scanner import Scanner
import sys

@click.command()
@click.argument('host', required=True, default="127.0.0.1")
@click.option("-s", "--sniff", required=False, is_flag=True, help="Sniff provided IP address")
@click.pass_obj
def cli(options, host, sniff):
    """
    Run IP commands
    """
    args = {
        'host': host,
    }

    if options.debug:
        click.echo(f'DEBUG ip:\nargs: {args}')

    scanner = Scanner(host)

    if sniff:
        scanner.sniff()
