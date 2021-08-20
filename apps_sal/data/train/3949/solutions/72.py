import math


def calculate_tip(amount, rating):
    try:
        k = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}[rating.lower()] * amount
    except:
        return 'Rating not recognised'
    return math.ceil(k)
