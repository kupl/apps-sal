def min_sum(a):
    a.sort()
    return sum([a[x] * a[-x - 1] for x in range(len(a) // 2)])
