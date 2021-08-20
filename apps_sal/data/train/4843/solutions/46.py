def best_choice(k, t, ls):
    if k == 0:
        return 0
    best = -1
    for (i, v) in enumerate(ls):
        if v > t:
            continue
        b = best_choice(k - 1, t - v, ls[i + 1:])
        if b < 0:
            continue
        b += v
        if b > best and b <= t:
            best = b
    return best


def choose_best_sum(t, k, ls):
    c = best_choice(k, t, ls)
    if c <= 0:
        return None
    else:
        return c
