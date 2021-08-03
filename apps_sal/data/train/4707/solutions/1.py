import re
from math import ceil


def to_bytes(n):
    return re.findall('.{8}', '{:0{}b}'.format(n, int(8 * ceil(n.bit_length() / 8.0)))) or [8 * '0']
