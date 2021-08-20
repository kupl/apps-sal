import math


def calculate_tip(amount, rating):
    try:
        return math.ceil(['terrible', 'poor', 'good', 'great', 'excellent'].index(rating.lower()) * 0.05 * amount)
    except:
        return 'Rating not recognised'
