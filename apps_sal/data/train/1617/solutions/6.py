from math import pi


def converter(n, decimals=0, base=pi):
    """takes n in base 10 and returns it in any base (default is pi
    with optional x decimals"""
    if n < 0:
        return '-' + converter(-n, decimals, base)
    CHARS = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    ln = 1
    while base ** ln <= n:
        ln += 1
    while 0 < ln:
        ln -= 1
        d = int(n / base ** ln)
        res += CHARS[d]
        n -= d * base ** ln
    if 0 < decimals:
        res += '.'
        base2 = 1
        while 0 < decimals:
            base2 *= 1 / base
            d = int(n / base2)
            res += CHARS[d]
            n -= d * base2
            decimals -= 1
    return res
