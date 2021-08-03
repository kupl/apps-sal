from statistics import mean, median


def mean_vs_median(numbers):
    avg, med = mean(numbers), median(numbers)
    return ["mean", "same", "median"][avg == med or avg < med and 2]
