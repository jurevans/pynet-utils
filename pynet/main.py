import click
import os

plugin_folder = os.path.join(os.path.dirname(__file__), 'commands')

class CLI(click.MultiCommand):
    def list_commands(self, _):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.startswith('__'):
                continue

            if filename.endswith('.py') and filename != '__init__.py':
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, _, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + '.py')
        with open(fn) as f:
            code = compile(f.read(), fn, 'exec')
            eval(code, ns, ns)
        return ns['cli']

class PyNet(object):
    def __init__(self, debug=False):
        self.debug = debug

@click.group(cls=CLI, help='Enter a subcommand')
@click.pass_context
@click.option("-d", "--debug", is_flag=True, help="Debug mode")
def cli(ctx, debug):
    ctx.obj = PyNet(debug)

if __name__ == '__main__':
    cli()
