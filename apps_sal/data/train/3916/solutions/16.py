def mean_vs_median(m):
    return (lambda mea, med: 'mean' if mea > med else 'median' if med > mea else 'same')(sum(m) / len(m), sorted(m)[len(m) // 2])
