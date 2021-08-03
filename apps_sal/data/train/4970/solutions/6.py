from collections import Counter


def vampire_test(x, y):
    return Counter(str(x)) + Counter(str(y)) == Counter(str(x * y))
