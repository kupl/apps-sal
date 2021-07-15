import socket
import struct

def numberAndIPaddress(s):
    if '.' in s:
        return str(struct.unpack('>I', socket.inet_aton(s))[0])
    else:
        return socket.inet_ntoa(struct.pack('>I', int(s)))
