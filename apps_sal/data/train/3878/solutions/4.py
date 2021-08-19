def kangaroo(kanga1, rate1, kanga2, rate2):
    s = kanga1 - kanga2
    v = rate1 - rate2
    return (s * v < 0) and not (s % v)  # czy jest podzielne
