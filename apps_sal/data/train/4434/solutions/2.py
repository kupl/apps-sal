from collections import Counter


def first_non_repeated(s):
    return next((k for k, v in Counter(s).items() if v == 1), None)
