def variance(words):
    from statistics import pvariance as var
    return round(var(len(word) for word in words), 4)

