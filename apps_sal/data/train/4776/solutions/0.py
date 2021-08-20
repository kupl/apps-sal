from itertools import islice, count


def u1():
    a = {1: 1, 2: 1}
    yield a[1]
    yield a[2]
    for n in count(3):
        a[n] = a[n - a[n - 1]] + a[n - a[n - 2]]
        yield a[n]


def length_sup_u_k(n, k):
    return len(list(filter(lambda x: x >= k, islice(u1(), 1, n))))


def comp(n):
    return sum((k1 < k0 for (k0, k1) in zip(list(islice(u1(), 1, n)), list(islice(u1(), 2, n)))))
