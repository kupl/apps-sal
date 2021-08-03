from ipaddress import IPv4Network, AddressValueError


def ipsubnet2list(subnet):
    try:
        return list(map(str, IPv4Network(subnet).hosts()))
    except AddressValueError:
        return None
