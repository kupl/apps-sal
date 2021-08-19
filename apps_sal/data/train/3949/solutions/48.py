import math


def calculate_tip(amount, rating):
    case = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    return 'Rating not recognised' if rating.lower() not in case else math.ceil(amount * case.get(rating.lower()))
