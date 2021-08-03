from collections import Counter


def points(s):
    m = tuple(sorted(dict(Counter(list(s))).values()))
    d = {(5,): 50, (1, 4): 40, (2, 3): 30}
    try:
        return d[m]
    except KeyError:
        return 20 if "".join(sorted(list(s))) in ["12345", "13456", "23456"] else 0
