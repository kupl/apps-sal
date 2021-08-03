from numpy import mean, median


def mean_vs_median(N):
    MEAN = int(mean(N))
    MEDIAN = int(median(N))
    return 'mean' if MEAN > MEDIAN else 'median' if MEDIAN > MEAN else 'same'
