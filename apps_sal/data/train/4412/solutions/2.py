from itertools import count


def rec(n):
    if not n:
        yield 0
        return
    for i in range(1 << (len(n) - 1)):
        tmp = [[], []]
        for t in n:
            i, r = divmod(i, 2)
            tmp[r].append(t)
        x, y = int(''.join(tmp[0])), tmp[1]
        for k in rec(y):
            yield x + k


def val(n): return sum(rec(str(n))) - n


def find(n, z):
    z += val(n)
    return next(i for i in count(n + 1) if val(i) > z)
