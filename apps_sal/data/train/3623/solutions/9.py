from collections import Counter


def product(s):
    return Counter(s).get("!", 0) * Counter(s).get("?", 0)
