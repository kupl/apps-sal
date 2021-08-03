import re


def ipv4_address(address):
    byte_reg = r'(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])'
    ipv4_regex = r'\A({0}[.]){{3}}{0}\Z'.format(byte_reg)
    return bool(re.match(ipv4_regex, address))
