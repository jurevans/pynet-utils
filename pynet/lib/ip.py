import ipaddress
import struct

PROTOCOL_MAP = {1: "ICMP", 6: "TCP", 17: "UDP"}


class IP:
    __slots__ = (
        "ver",
        "ihl",
        "tos",
        "len",
        "id",
        "offset",
        "ttl",
        "protocol_num",
        "sum",
        "src",
        "dst",
        "src_address",
        "dst_address",
        "protocol",
    )

    def __init__(self, buff):
        header = struct.unpack("<BBHHHBBH4s4s", buff)
        self.ver = header[0] >> 4
        self.ihl = header[0] & 0xF

        self.tos: int = header[1]
        self.len: int = header[2]
        self.id: str = header[3]
        self.offset: int = header[4]
        self.ttl: int = header[5]
        self.protocol_num: int = header[6]
        self.sum: int = header[7]
        self.src: str = header[8]
        self.dst: str = header[9]

        self.src_address: str = ipaddress.ip_address(self.src)
        self.dst_address: str = ipaddress.ip_address(self.dst)

        try:
            self.protocol: str = PROTOCOL_MAP[self.protocol_num]
        except Exception as e:
            print("%s No protocol for %s" % e, self.protocol_num)
