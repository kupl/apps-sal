from statistics import *


def mean_vs_median(ns):
    (a, b) = (mean(ns), median(ns))
    return ('same', 'mean', 'median')[(a > b) - (a < b)]
