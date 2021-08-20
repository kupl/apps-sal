from statistics import mean, median


def mean_vs_median(numbers):
    (mn, md) = (mean(numbers), median(numbers))
    return ['median', 'same', 'mean'][(mn > md) - (mn < md) + 1]
