from statistics import mean, median
from numpy import sign

def mean_vs_median(numbers):
    return ("same", "mean", "median")[int(sign(mean(numbers) - median(numbers)))]
