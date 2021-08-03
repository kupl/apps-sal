from ipaddress import IPv4Address


def numberAndIPaddress(s):
    return str(int(IPv4Address(s))) if '.' in s else str(IPv4Address(int(s)))
