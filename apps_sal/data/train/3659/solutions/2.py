from statistics import pvariance as var

variance = lambda words: round(var(len(word) for word in words), 4)
