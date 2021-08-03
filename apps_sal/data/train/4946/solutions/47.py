from itertools import takewhile


def house_numbers_sum(lst): return sum(takewhile(lambda n: n != 0, lst))
