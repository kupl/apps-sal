def calc_tip(p, r):
    if p % 10 < 5:
        p //= 10
    else:
        p = p // 10 + 1
    if r == 1:
        tip = p + 1
    elif r == 0:
        tip = p - 1
    else:
        tip = int(p/2) - 1
    return tip if tip >= 0 else 0
