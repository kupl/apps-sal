from statistics import mean, median


def mean_vs_median(numbers):
    mn = mean(numbers)
    md = median(numbers)
    return 'mean' if mn > md else 'median' if md > mn else 'same'
