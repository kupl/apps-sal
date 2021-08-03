from ipaddress import IPv4Address


def numberAndIPaddress(string):
    if '.' in string:
        return str(int(IPv4Address(string)))
    return str(IPv4Address(int(string)))
