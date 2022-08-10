import click
from pynet.lib.udp import UDP
import sys

@click.command()
@click.option("-h", "--host", required=False, help="Host to send UDP packets to")
@click.option("-s", "--subnet", required=False, help="Subnet to send UDP packets to")
@click.option("-m", "--message", required=False, help="Message to send in UDP packets")
@click.option("-v", "--verbose", required=False, is_flag=True, help="Enable verbose flag")
@click.pass_obj
def cli(options, host, subnet, message, verbose):
    """
    Run UDP commands
    """
    args = {
        'host': host,
        'subnet': subnet,
        'message': message,
        'verbose': verbose or options.debug
    }

    if not host and not subnet:
        click.echo(f'You must provide either a host or a subnet!')
        return

    if options.debug:
        click.echo(f'DEBUG udp:\nargs: {args}')

    udp = UDP(args)
    udp.send()
