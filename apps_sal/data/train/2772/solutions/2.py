import time


def mystery(n):
    c = 0
    begin = time.time()
    end = time.time()
    limit = 0.2
    while n != 1 and n != 13 and n < 1000000 and end - begin < limit:
        c += 1
        if n & 1:
            n = n + n + n + n + n + 1
        else:
            n = n >> 1
        end = time.time()
    return (c, -1)[end - begin > limit]


def wrap_mystery(n):
    return mystery(n)
