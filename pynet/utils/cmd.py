import shlex
import subprocess


def execute(cmd: str) -> str | None:
    cmd = cmd.strip()
    if not cmd:
        return None
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output.decode()
