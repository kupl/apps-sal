def abundant(h):
    s = sigma(h)
    while s < h:
        h -= 1
        s = sigma(h)
    return [[h], [s - h]]


def sigma(x):
    (sq, s, i) = (x ** 0.5, 1, 2)
    while i <= sq:
        if x % i == 0:
            s += i + x / i
        if i == sq:
            s -= i
        i += 1
    return s
