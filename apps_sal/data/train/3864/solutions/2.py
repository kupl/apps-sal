from ipaddress import ip_address

def int32_to_ip(int32):
    return str(ip_address(int32))
