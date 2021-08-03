from operator import mul
from functools import reduce


def string_color(s):
    if len(s) > 1:
        a = [ord(x) for x in s]
        n = sum(a)
        return f"{n%256:02X}{reduce(mul, a) % 256:02X}{abs(a[0] * 2 - n) % 256:02X}"
