def min_unfairness(a, k):
    return a.sort() or (k > 0 < len(a) and min((b - a for (a, b) in zip(a, a[k - 1:]))))
