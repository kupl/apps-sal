from statistics import mean, median


def mean_vs_median(numbers):
    (m1, m2) = (mean(numbers), median(numbers))
    return [['median', 'mean'][m1 > m2], 'same'][m1 == m2]
