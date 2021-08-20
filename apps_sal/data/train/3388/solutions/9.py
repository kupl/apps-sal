import re


def binary_to_string(binary):
    return ''.join((chr(int(e, 2)) for e in re.findall('.' * 8, binary)))
