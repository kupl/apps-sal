def mystery(n):
    c, seen = 0, set()
    while n != 1 and n != 13 and n < 1000000:
        c += 1
        if n & 1:
            n = n + n + n + n + n + 1
        else:
            n = n >> 1
        if n not in seen:
            seen.add(n)
        else:
            return -1
    return c


def wrap_mystery(n):
    return mystery(n)
