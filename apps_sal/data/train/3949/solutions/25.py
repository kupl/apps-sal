import math


def calculate_tip(amount, rating):
    rating = rating.lower()
    if rating == 'terrible':
        return 0
    if rating == 'poor':
        return int(math.ceil(amount * 0.05))
    if rating == 'good':
        return int(math.ceil(amount * 0.1))
    if rating == 'great':
        return int(math.ceil(amount * 0.15))
    if rating == 'excellent':
        return int(math.ceil(amount * 0.2))
    else:
        return 'Rating not recognised'
