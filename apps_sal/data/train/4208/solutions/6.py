from ipaddress import IPv4Network, AddressValueError


def ipsubnet2list(subnet):
    try:
        ip_list = [str(ip) for ip in IPv4Network(subnet)]
        return ip_list[1:-1] if len(ip_list) > 2 else ip_list
    except AddressValueError:
        return None
