from collections import Counter


def odd_ones_out(numbers):
    return [x for x in numbers if x in [k for k, v in Counter(numbers).items() if v % 2 == 0]]
