def value_at(p, x):
    return round(sum((c * choose(x, len(p) - 1 - i) for (i, c) in enumerate(p))), 2)


def choose(x, k):
    (n, d) = (1, 1)
    for i in range(k):
        (n, d) = (n * (x - i), d * (i + 1))
    return n / d
