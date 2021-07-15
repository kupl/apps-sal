from itertools import takewhile

def house_numbers_sum(arr):
    return sum(takewhile(lambda x: x != 0, arr))
