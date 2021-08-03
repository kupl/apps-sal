def choose_best_sum(t, k, ls):
    res = cbs(t, k, list(reversed(sorted(ls))))
    return res if res > 0 else None


minf = float("-inf")


def cbs(t, k, ls):
    while ls and ls[0] > t:
        del ls[0]
    if len(ls) < k:
        return minf
    if k == 1:
        return ls[0]
    return max(ls[0] + cbs(t - ls[0], k - 1, ls[1:]), cbs(t, k, ls[1:]))
