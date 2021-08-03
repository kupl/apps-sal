import re


def mid_endian(n):
    h = hex(n)[2:].upper()
    r = re.findall('..', '0' * (len(h) % 2) + h)
    return "".join(r[1::2][::-1] + r[0::2])
