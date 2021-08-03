def recurse(sum, ls, level):
    if level == 1:
        return [(x + sum) for x in ls]
    ary = list(ls)
    totals = []
    for x in ls:
        ary.remove(x)
        if len(ary) >= level - 1:
            totals += recurse(sum + x, ary, level - 1)
    return totals


def choose_best_sum(t, k, ls):
    if len(ls) < k:
        return None
    totals = recurse(0, ls, k)
    sum = 0
    for x in totals:
        if x > sum and x <= t:
            sum = x
    if sum == 0:
        return None
    return sum
