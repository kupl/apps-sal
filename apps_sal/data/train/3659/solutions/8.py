from collections import Counter
from numpy import average

def variance(words):
    values, weights = zip(*Counter(map(len, words)).items())
    return round(average((values-average(values, weights=weights))**2, weights=weights), 4)
