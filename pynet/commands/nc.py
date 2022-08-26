import click
from pynet.lib.nc import NC
import sys

@click.command()
@click.option("-h", "--host", required=False, default="0.0.0.0", help="Host URL - defaults to 0.0.0.0")
@click.option("-p", "--port", required=True, type=click.INT, help="Port number")
@click.option("-l", "--listen", is_flag=True, help="Enable listen mode")
@click.option("-e", "--execute", required=False, help="Execute command, return output")
@click.option("-c", "--command", is_flag=True, required=False, help="Return a command shell")
@click.option("-u", "--upload", required=False, help="File to upload")
@click.pass_obj
def cli(options, host, port, listen, execute, command, upload) -> None:
    """
    Run netcat-like commands
    """
    args = {
        'host': host,
        'port': port,
        'command': command,
        'execute': execute,
        'listen': listen,
        'upload': upload,
    }

    if options.debug:
        click.echo(f'DEBUG nc:\nargs: {args}')

    buffer = '' if listen else sys.stdin.read()
    nc = NC(args, buffer, debug=options.debug)
    nc.run()
