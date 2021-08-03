N = 10_000
a = [1] * N
a[0] = a[1] = 0
for i in range(2, N):
    if a[i]:
        for j in range(i**2, N, i):
            a[j] = 0
a = [i for i, x in enumerate(a) if x]


def solve(n, m):
    return all(not n % x for x in f(m))


def f(n):
    s = set()
    for x in a:
        if x > n:
            break
        while not n % x:
            n //= x
            s.add(x)
    if n > 1:
        s.add(n)
    return s
