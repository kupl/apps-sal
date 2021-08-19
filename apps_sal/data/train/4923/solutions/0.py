from collections import Counter


def count_feelings(s, arr):
    total = sum((Counter(s) & Counter(w) == Counter(w) for w in arr))
    return '%s feeling%s.' % (total, '' if total == 1 else 's')
