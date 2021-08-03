from functools import reduce


def greatest_product(n):
    test = [reduce((lambda x, y: x * y), list(map(int, n[i:i + 5]))) for i in range(0, len(n) - 4)]
    return max(test)
