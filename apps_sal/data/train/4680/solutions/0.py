BASE = {"H": 50, "Q": 25, "D": 10, "N": 5, "P": 1}


def make_change(n):
    r = {}
    for x, y in BASE.items():
        if n >= y:
            r[x], n = divmod(n, y)
    return r
