import math


def calculate_tip(amount, rating):
    if rating.lower() == 'poor':
        return math.ceil(0.05 * amount)
    if rating.lower() == 'good':
        return math.ceil(0.1 * amount)
    if rating.lower() == 'great':
        return math.ceil(0.15 * amount)
    if rating.lower() == 'excellent':
        return math.ceil(0.2 * amount)
    if rating.lower() == 'terrible':
        return 0
    return 'Rating not recognised'
