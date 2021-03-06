import math


def calculate_tip(amount, rating):
    rates = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    return math.ceil(amount * rates[rating.lower()]) if rating.lower() in rates.keys() else 'Rating not recognised'
