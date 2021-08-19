from collections import Counter


def count_feelings(s, arr):
    sc = Counter(s)
    n = sum((all((sc[c] >= x for (c, x) in Counter(feeling).items())) for feeling in arr))
    return f"{n} feeling{('' if n == 1 else 's')}."
