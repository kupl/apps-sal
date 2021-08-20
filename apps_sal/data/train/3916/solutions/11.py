def mean_vs_median(n):
    return 'mean' if sum(n) / len(n) > n[int(len(n) / 2)] else 'same' if sum(n) / len(n) == n[int(len(n) / 2) + 1] else 'median'
