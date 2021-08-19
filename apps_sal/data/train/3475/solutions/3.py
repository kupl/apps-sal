import re
BASE = {'0b': 2, '0x': 16, '0o': 8, '': 10}


def to_integer(string):
    matched = re.search('\\A(?P<sign>[-+]?)(?P<base>0[box]|)?(?P<n>[a-fA-F0-9]+)\\Z', string)
    if not matched:
        return None
    base = BASE[matched.group('base').lower()]
    try:
        n = int(matched.group('n'), base)
    except ValueError:
        return None
    return n * (-1 if matched.group('sign') == '-' else 1)
