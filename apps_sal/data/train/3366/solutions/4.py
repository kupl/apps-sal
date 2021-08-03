from math import factorial


def nth_perm(n, d):
    n = n - 1
    lst = sorted(map(str, range(d)))
    f = factorial(d)
    ans = []
    while lst:
        f = f // len(lst)
        c, n = n // f, n % f
        ans += [lst.pop(c)]
    return ''.join(map(str, ans))
