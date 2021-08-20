def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def count_ones(n):
    a = [6, 7]
    for i in range(2, n + 1):
        a.append(a[i - 1] + gcd(i, a[i - 1]))
    return sum([a[i + 1] - a[i] == 1 for i in range(n)])


def max_pn(n):
    (a, p, i) = (7, {1}, 1)
    while len(p) < n + 1:
        i += 1
        b = a + gcd(i, a)
        p.add(b - a)
        a = b
    return max(p)


def an_over_average(n):
    return 3
