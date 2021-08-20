from math import ceil


def pay_cheese(a):
    return f'L{round(ceil(sum(a) * 6.0 / 10.0 / 60.0) * 35)}'
