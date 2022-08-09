import click
from lib.nc import NC

@click.command()
@click.option("-h", "--host", required=False, default="0.0.0.0", help="Host URL - defaults to 0.0.0.0")
@click.option("-p", "--port", required=True, help="Port number")
@click.option("-l", "--listen", is_flag=True, help="Enable listen mode")
@click.option("-e", "--exec", required=False, help="Command to execute")
@click.option("-u", "--upload", required=False, help="File to upload")
@click.pass_obj
def cli(options, host, port, listen, exec, upload):
    """Run netcat-like commands"""

    if options.debug:
        print(f"Host: {host}")
        print(f"Port: {port}")
        print(f"Listen?: {listen}")
        print(f"Exec: {exec}")
        print(f"Upload: {upload}")
