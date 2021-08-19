def min_sum(a):
    a.sort()
    return sum((a[i] * a[~i] for i in range(len(a) // 2)))
