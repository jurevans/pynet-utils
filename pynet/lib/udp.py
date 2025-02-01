import ipaddress
import socket


class UDP:
    def __init__(self, args):
        self.host = args["host"]
        self.subnet = args["subnet"]
        self.message = args["message"]
        self.verbose = args["verbose"]
        self.sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send(self) -> None:
        if self.subnet:
            try:
                for ip in ipaddress.ip_network(self.subnet):
                    if self.verbose:
                        print(f"Sending DGRAM to {ip}")
                    self.sender.sendto(bytes(self.message, "utf8"), (str(ip), 65212))
            except Exception as e:
                print(f"Encountered an error: {e}")
            return

        if self.host:
            try:
                ip = ipaddress.ip_address(self.host)
                if self.verbose:
                    print(f"Sending DGRAM to {ip}")
                self.sender.sendto(bytes(self.message, "utf8"), (str(ip), 65212))
            except Exception as e:
                print(f"Encountered an error: {e}")
            return
