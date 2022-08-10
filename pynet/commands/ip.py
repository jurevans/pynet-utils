import click
from pynet.lib.ip import IP
import sys

@click.command()
@click.argument('host', required=True, default="127.0.0.1")
@click.option("-s", "--sniff", required=False, is_flag=True, help="Sniff provided IP address")
@click.pass_obj
def cli(obj, host, sniff):
    """
    Run IP commands
    """
    args = {
        'host': host,
    }

    if obj.debug:
        click.echo(f'DEBUG ip:\nargs: {args}')

    if sniff:
        IP.sniff(host)
