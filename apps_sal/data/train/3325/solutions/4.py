from collections import Counter


def most_common(s):
    count = Counter(s)
    return ''.join((t[2] for t in sorted(((-count[c], i, c) for (i, c) in enumerate(s)))))
