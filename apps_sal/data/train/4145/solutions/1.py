from socket import inet_aton, inet_ntoa
from struct import Struct

Addr = Struct('>I')

def ipv4__parser(ip_addr, mask):
    i, = Addr.unpack(inet_aton(ip_addr))
    m, = Addr.unpack(inet_aton(mask))
    return inet_ntoa(Addr.pack(i&m)), inet_ntoa(Addr.pack(i&~m))
