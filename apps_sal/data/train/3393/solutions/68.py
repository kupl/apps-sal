from math import sqrt


def sumsqrdivs(x):
    divs = []
    for i in range(1, int(sqrt(x) + 1)):
        if x % i == 0:
            divs.append(i)
            if i**2 != x:
                divs.append(int(x / i))
    return sum(div**2 for div in divs)


def list_squared(m, n):
    return [[i, sumsqrdivs(i)] for i in range(m, n + 1) if sqrt(sumsqrdivs(i)).is_integer()]
