from statistics import *


def mean_vs_median(numbers):
    (a, b) = (mean(numbers), median(numbers))
    return ('same', 'mean', 'median')[(a > b) - (a < b)]
