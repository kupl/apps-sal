import math


def calculate_tip(amount, rating):
    rating = rating.lower()
    if rating == 'terrible':
        return math.ceil(amount * 0)
    if rating == 'poor':
        return math.ceil(amount * 0.06)
    if rating == 'good':
        return math.ceil(amount * 0.1)
    if rating == 'great':
        return math.ceil(amount * 0.15)
    if rating == 'excellent':
        return math.ceil(amount * 0.2)
    else:
        return 'Rating not recognised'
