import socket


def ipv4_address(address):
    try:
        socket.inet_pton(socket.AF_INET, address)
        return True
    except socket.error:
        return False
