from re import findall
from functools import reduce


def mid_endian(n):
    return reduce(lambda a, b: b[1] + a if b[0] % 2 else a + b[1], enumerate(findall('.{2}', (lambda h: ('0' if len(h) % 2 else '') + h)(hex(n)[2:].upper()))), '')
