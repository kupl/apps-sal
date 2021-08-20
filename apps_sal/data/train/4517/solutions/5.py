from collections import Counter


def odd_one_out(s):
    return sorted((x for (x, i) in list(Counter(s).items()) if i % 2), key=s.rfind)
