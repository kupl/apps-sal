import math


def pay_cheese(arr):
    return f'L{round(math.ceil(sum(map(lambda x: x / 100, arr))) * 4 * 8.75)}'
