def memoize(func):
    cache = {}
    def newfunc(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return newfunc

@memoize
def fusc(n):
    assert type(n) == int and n >= 0
    if n < 2: return n
    return fusc(n / 2) + fusc(n / 2 + 1) if n % 2 else fusc(n / 2)

