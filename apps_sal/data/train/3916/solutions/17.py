from numpy import median, mean


def mean_vs_median(lst):
    (avg, med) = (mean(lst), median(lst))
    return 'same' if avg == med else 'mean' if avg > med else 'median'
