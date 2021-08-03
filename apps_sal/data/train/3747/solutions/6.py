from ipaddress import ip_address


def ipv4_address(address: str) -> bool:
    try:
        return len(str(ip_address(address))) == len(address)
    except ValueError:
        return False
