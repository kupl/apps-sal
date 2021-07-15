def evaporator(content, e_p_d, thresh):
    n = 0
    start_ = 100
    per_ = 1 - e_p_d / 100.0
    while start_ > thresh:
        start_ *= per_
        n += 1
    return n
