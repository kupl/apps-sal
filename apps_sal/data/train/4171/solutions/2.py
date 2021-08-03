from collections import Counter

# Only work in 3.6+ because dicts are ordered


def no_repeat(string):
    return next(k for k, v in Counter(string).items() if v == 1)
