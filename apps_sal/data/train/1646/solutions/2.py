GREENS = [0, 1, 5, 6]
(a, b) = GREENS[-2:]
base = 10


def is_green(n):
    return n * n % (base * 10) == n


while len(GREENS) <= 5000:
    for x in range(base, base * 10, base):
        (a_, b_) = (x + a, x + b)
        if a < base and is_green(a_):
            GREENS.append(a_)
            a = a_
        if b < base and is_green(b_):
            GREENS.append(b_)
            b = b_
    base *= 10


def green(n):
    return GREENS[n]
