def kangaroo(kanga1, rate1, kanga2, rate2):
    if kanga1 < kanga2 and rate1 <= rate2 or kanga1 > kanga2 and rate1 >= rate2:
        return False
    else:
        return ((kanga1 - kanga2) / (rate2 - rate1)) % 1 == 0
