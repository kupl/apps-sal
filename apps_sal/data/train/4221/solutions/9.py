def count_targets(n, a):
    res = 0
    for i, v in enumerate(a):
        if i - n < 0:
            continue
        if v == a[i - n]:
            res += 1
    return res
