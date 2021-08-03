from re import match


def ipv4_address(address):
    return bool(match(r'^(([1-9]?\d|1\d{2}|2([0-4]\d|5[0-5]))(\.(?!$)|$)){4}\Z', address))
