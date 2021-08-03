def calc_tip(p, r):
    if int(str(p)[-1]) < 5:
        p -= int(str(p)[-1])
    else:
        p += 10 - int(str(p)[-1])
    if len(str(p)) >= 2:
        T = int(str(p)[:-1])
    else:
        T = 0
    if r == 1:
        return T + 1
    elif r == 0:
        return max(T - 1, 0)
    else:
        return max(T // 2 - 1, 0)
