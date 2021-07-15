from statistics import pvariance

def variance(words):
    return round(pvariance(map(len, words)), 4)
