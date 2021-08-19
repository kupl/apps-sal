def variance(w):
    return round(__import__('statistics').pvariance(map(len, w)), 4)
