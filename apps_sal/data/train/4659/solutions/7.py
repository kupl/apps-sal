from ipaddress import ip_address


def numberAndIPaddress(s):
    return str(int(ip_address(s)) if '.' in s else ip_address(int(s)))
