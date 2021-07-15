from numpy import mean, median
def mean_vs_median(n):
    return 'mean' if mean(n) > median(n) else 'median' if median(n) > mean(n) else 'same'
