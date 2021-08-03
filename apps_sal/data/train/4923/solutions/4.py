from collections import Counter


def count_feelings(s, arr):
    count = sum(1 for f in arr if not Counter(f) - Counter(s))
    return '{} feeling{}.'.format(count, '' if count == 1 else 's')
