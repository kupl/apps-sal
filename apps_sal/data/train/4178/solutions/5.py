def min_sum(a):
    return a.sort() or sum((a[i] * a[-i - 1] for i in range(len(a) // 2)))
