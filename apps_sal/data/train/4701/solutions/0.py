from math import ceil
def pay_cheese(arr):
    return f'L{ceil(sum(arr) / 100) * 35}'
