from fractions import gcd


def seq():
    (i, a, g) = (1, 7, 1)
    while 1:
        yield (i, a, g)
        i += 1
        g = gcd(i, a)
        a += g


def count_ones(n):
    return sum((g == 1 for (_, (i, a, g)) in zip(range(n), seq())))


def p(n):
    seen = set()
    for (i, a, g) in seq():
        if not n:
            break
        if g > 1 and g not in seen:
            n -= 1
            seen.add(g)
            yield g


def max_pn(n):
    return max(p(n))


def an_over(n):
    for (i, a, g) in seq():
        if not n:
            break
        if g > 1:
            n -= 1
            yield (a / i)


def an_over_average(n):
    return sum(an_over(n)) / n
