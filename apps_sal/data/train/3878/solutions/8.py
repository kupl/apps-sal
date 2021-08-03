def kangaroo(kanga1, rate1, kanga2, rate2):
    if rate1 == rate2:
        return kanga1 == kanga2
    time_ = (kanga2 - kanga1) / (rate1 - rate2)
    return time_ > 0 and time_.is_integer()
