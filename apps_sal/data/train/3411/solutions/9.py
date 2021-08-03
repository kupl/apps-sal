def amort(r, b, t, n):
    r /= 1200
    c = r * b / (1 - (1 + r)**-t)
    for i in range(n):
        I, p, b = r * b, c - r * b, r * b + b - c
    return "num_payment %d c %.0f princ %.0f int %.0f balance %.0f" % (n, c, p, I, b)
