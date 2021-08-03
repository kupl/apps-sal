from numpy import mean, median


def mean_vs_median(numbers):
    if mean(numbers) > median(numbers):
        return 'mean'
    elif mean(numbers) < median(numbers):
        return 'median'
    else:
        return 'same'
