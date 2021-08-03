from statistics import pvariance as var


def variance(words): return round(var(len(word) for word in words), 4)
