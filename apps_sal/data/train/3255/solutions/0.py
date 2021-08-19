from collections import Counter


def only_duplicates(string):
    cs = Counter(string)
    return ''.join((c for c in string if cs[c] > 1))
