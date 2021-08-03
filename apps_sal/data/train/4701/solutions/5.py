from math import ceil


def pay_cheese(arr):
    p = ceil(sum(arr) * 6 / 600)
    return 'L{}'.format(int(p * 8.75 * 4))
