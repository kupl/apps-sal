from functools import reduce


def greatest_product(n):
    l = list(map(int, list(n)))
    return max([reduce(lambda x, y:x * y, l[i:i + 5]) for i in range(len(l)) if len(l[i:i + 5]) == 5])
