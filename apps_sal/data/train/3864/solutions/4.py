import ipaddress
def int32_to_ip(int32):
    return str(ipaddress.IPv4Address(int32))

