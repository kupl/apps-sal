def kangaroo(kanga1, rate1, kanga2, rate2):
    d = kanga1 - kanga2
    s = rate1 - rate2
    return d * s < 0 and (not d % s)
