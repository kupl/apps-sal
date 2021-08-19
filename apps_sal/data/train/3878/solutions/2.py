def kangaroo(kanga1, rate1, kanga2, rate2):
    (k, r) = (kanga1 - kanga2, rate2 - rate1)
    return k % r == 0 if k * r > 0 else k == r
