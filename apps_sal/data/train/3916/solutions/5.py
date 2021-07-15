from statistics import mean
from statistics import median

def mean_vs_median(n):
    return "mean" if mean(n)>median(n) else "median" if mean(n)<median(n) else "same"

