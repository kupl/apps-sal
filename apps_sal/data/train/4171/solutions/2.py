from collections import Counter


def no_repeat(string):
    return next((k for (k, v) in Counter(string).items() if v == 1))
