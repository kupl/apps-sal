import ipaddress
def ips_between(start, end):
    # TODO
    one = int(ipaddress.IPv4Address(start))
    two = int(ipaddress.IPv4Address(end))
    return two-one
