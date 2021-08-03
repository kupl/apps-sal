from collections import Counter


def array_equalization(a, k):
    n = len(a)
    freq = Counter(a)
    m = n
    for number in freq.keys():
        c = 0
        i = 0
        while i < len(a):
            if a[i] != number:
                c += 1
                i += k
            else:
                i += 1
        m = min(c, m)
    return m
