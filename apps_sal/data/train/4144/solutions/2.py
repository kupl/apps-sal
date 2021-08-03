def ab(n):
    s = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s += i
            if i * i != n:
                s += n // i
    return s - n


def abundant(h):
    for i in range(h, 0, -1):
        a = ab(i)
        if a > 0:
            return [[i], [a]]
