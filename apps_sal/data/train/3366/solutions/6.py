from math import factorial


def nth_perm(n, d):
    (n, ds, res) = (n - 1, list(range(d)), [])
    for i in range(d - 1, -1, -1):
        (p, n) = divmod(n, factorial(i))
        res.append(ds.pop(p))
    return ''.join(map(str, res))
