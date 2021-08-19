from bisect import bisect_left
N = 100000
a = [1] * N
a[0] = a[1] = 0
for i in range(2, N):
    if a[i]:
        for j in range(i ** 2, N, i):
            a[j] = 0
a = [i for (i, x) in enumerate(a) if x]


def is_prime_happy(n):
    return n > 2 and (not sum(a[:bisect_left(a, n)]) % n)
