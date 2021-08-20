from statistics import mean, median


def mean_vs_median(numbers):
    (mn, md) = (mean(numbers), median(numbers))
    return 'mean' if mn > md else 'median' if md > mn else 'same'
