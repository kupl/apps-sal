import struct
from socket import inet_aton


def ip_to_int32(ip):
    return struct.unpack('>I', inet_aton(ip))[0]
