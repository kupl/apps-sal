import math


def calculate_tip(amount, rating):
    ratings = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    return math.ceil(amount * ratings.get(rating.lower(), 0)) if rating.lower() in ratings else 'Rating not recognised'
