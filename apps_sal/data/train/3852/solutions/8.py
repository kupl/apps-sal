import ipaddress


def ips_between(start, end):
    one = int(ipaddress.IPv4Address(start))
    two = int(ipaddress.IPv4Address(end))
    return two - one
