import socket
def ipv4_address(address):
    try: # No need to do work that's already been done
        socket.inet_pton(socket.AF_INET,address)
        return True
    except socket.error: # Better to ask forgiveness than permission
        return False
