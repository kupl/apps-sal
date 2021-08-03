def recurse(p, s, n, start):
    k = n + p - s
    if k > kmax:
        return
    if p < N[k]:
        N[k] = p
    for x in range(start, 2 * kmax // p + 1):
        recurse(p * x, s + x, n + 1, x)


kmax = 12000
N = [3 * kmax] * (kmax + 1)
recurse(1, 0, 0, 2)


def productsum(n):
    return sum(set(N[2:n + 1]))
