from collections import Counter


def common(a, b, c):
    abc = Counter(a) & Counter(b) & Counter(c)
    return sum(abc.elements())
