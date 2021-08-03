def mean_vs_median(a):
    m = sum(a) / len(a)
    a.sort()
    x = a[len(a) // 2]
    return 'same' if m == x else 'mean' if m > x else 'median'
