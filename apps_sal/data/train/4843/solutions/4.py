def choose_best(t, k, ls):
    if k == 0:
        return 0
    best = -1
    for (i, v) in enumerate(ls):
        if v > t:
            continue
        b = choose_best(t - v, k - 1, ls[i + 1:])
        if b < 0:
            continue
        b += v
        if b > best and b <= t:
            best = b
    return best


def choose_best_sum(t, k, ls):
    c = choose_best(t, k, ls)
    if c <= 0:
        return None
    return c
