(i, j, k, n) = (5, 6, 1, 0)
l = [1]
while n < 5000:
    k = 10 * k
    i = i ** 2 % k
    j = (1 - (j - 1) ** 2) % k
    l.extend(sorted((x for x in [i, j] if x not in l)))
    n = n + 1


def green(n):
    return l[n - 1]
