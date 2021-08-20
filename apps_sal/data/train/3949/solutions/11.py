import math


def calculate_tip(amount, rating):
    tip = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    return 'Rating not recognised' if rating.lower() not in tip else math.ceil(amount * tip[rating.lower()])
