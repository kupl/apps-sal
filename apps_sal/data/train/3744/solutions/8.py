d = {}


def odd(n):
    if n == -1:
        return 10**1000
    r = 0
    while n % 2:
        r += 1
        n = (n - 1) // 2
    return r


def oddest(a):
    if not a:
        return
    o = [*map(odd, a)]
    if o.count(max(o)) > 1:
        return
    return max(a, key=odd)
