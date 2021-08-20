def kangaroo(kanga1, rate1, kanga2, rate2):
    if kanga1 > kanga2 and rate1 >= rate2 or (kanga2 > kanga1 and rate2 >= rate1):
        return False
    if 1 - abs(kanga1 - kanga2) % abs(rate1 - rate2) < 0:
        return False
    return 1 - abs(kanga1 - kanga2) % abs(rate1 - rate2)
