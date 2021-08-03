from functools import lru_cache


@lru_cache(maxsize=None)
def balanced_parens(n):
    if not n:
        return [""]
    r = set()
    for x in balanced_parens(n - 1):
        r.add("(" + x + ")")
    for i in range(1, n // 2 + 1):
        lo = balanced_parens(i)
        hi = balanced_parens(n - i)
        for x in lo:
            for y in hi:
                r.add(x + y)
                r.add(y + x)
    return list(r)
