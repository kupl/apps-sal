from re import compile, match
REGEX = compile('((\\d|[1-9]\\d|1\\d\\d|2[0-4]\\d|25[0-5])\\.){4}$')


def ipv4_address(address):
    return bool(match(REGEX, address + '.'))
