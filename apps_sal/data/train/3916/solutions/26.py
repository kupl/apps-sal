from statistics import mean, median


def mean_vs_median(numbers):
    avg, med = mean(numbers), median(numbers)
    return "same" if avg == med else "mean" if avg > med else "median"
