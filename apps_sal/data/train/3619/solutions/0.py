from collections import Counter


def is_dd(n):
    return any(value == count for value, count in Counter(int(x) for x in str(n)).items())
