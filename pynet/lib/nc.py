import socket
import sys
import threading

from pynet.utils.cmd import execute

"""
Small library to provide minimal Netcat-like functionality
"""


class NC:
    def __init__(self, args, buffer=None, debug=False):
        self.args = args
        self.buffer = buffer
        self.debug: bool = debug
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self) -> None:
        if self.debug:
            print("NC.run()")
        if self.args["listen"]:
            self.listen()
        else:
            self.send()

    def send(self) -> None:
        if self.debug:
            print("NC.send()")
        try:
            self.socket.connect((self.args["host"], self.args["port"]))
        except Exception as e:
            print(
                f"Failed to connect to host {self.args['host']} on port {self.args['port']}\n{e}"
            )
            sys.exit()

        print(self.buffer)
        if self.buffer:
            if self.debug:
                print("self.socket.send()")
            self.socket.send(self.buffer)

        try:
            while True:
                recv_len = 1
                response = ""
                while recv_len:
                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    if recv_len < 4096:
                        break

                    if response:
                        print(response)
                        buffer = input("#> ")
                        buffer += "\n"
                        self.socket.send(buffer.encode())

        except KeyboardInterrupt:
            print("User terminated.")
            self.socket.close()
            sys.exit()

    def listen(self) -> None:
        if self.debug:
            print("NC.listen()")
        self.socket.bind((self.args["host"], self.args["port"]))
        self.socket.listen(5)

        while True:
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(target=self.handle, args=(client_socket,))
            client_thread.start()

    def handle(self, client_socket) -> None:
        if self.args["execute"]:
            output = execute(self.args["execute"])
            if output != None:
                client_socket.send(output.encode())

        elif self.args["upload"]:
            file_buffer = b""

            while True:
                data = client_socket.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break

            with open(self.args["upload"]) as f:
                f.write(str(file_buffer))

                message = f"Saved file {self.args['upload']}"
                client_socket.send(message.encode())

        elif self.args["command"]:
            cmd_buffer = b""

            while True:
                try:
                    client_socket.send(b"#> ")
                    while "\n" not in cmd_buffer.decode():
                        cmd_buffer += client_socket.recv(64)
                    response = execute(cmd_buffer.decode())
                    if response:
                        client_socket.send(response.encode())
                    cmd_buffer = b""
                except Exception as e:
                    print(f"Server killed! {e}")
                    self.socket.close()
                    sys.exit()
