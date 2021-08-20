import re


def is_mac_48_address(address):
    return bool(re.match('^([0-9A-F]{2}[-]){5}([0-9A-F]{2})$', address.upper()))
