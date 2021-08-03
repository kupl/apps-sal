from socket import inet_aton, inet_ntoa
from struct import unpack, pack


def to_int(s): return unpack(">L", inet_aton(s))[0]


def to_ip(x): return inet_ntoa(pack('>L', x))


def ipv4__parser(ip_addr, mask):
    ip, m = to_int(ip_addr), to_int(mask)
    return to_ip(ip & m), to_ip(ip & ~m)
