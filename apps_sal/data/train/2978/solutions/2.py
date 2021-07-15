from collections import Counter


def count_sel(lst):
    c = Counter(lst)
    m = max(c.values())
    return [
        len(lst),
        len(c),
        sum(x == 1 for x in c.values()),
        [sorted(k for k, v in c.items() if v == m), m,],
    ]
