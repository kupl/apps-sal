import math


def calculate_tip(amount, rating):
    d = {'terrible': 0.0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    return 'Rating not recognised' if rating.lower() not in d.keys() else math.ceil(amount * d.get(rating.lower()))
