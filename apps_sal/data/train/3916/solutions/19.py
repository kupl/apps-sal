from numpy import mean, median

def mean_vs_median(numbers):
    meann = mean(numbers)
    mediann = median(numbers)
    if meann == mediann:
        return "same"
    elif meann > mediann:
        return "mean"
    else:
        return "median"

