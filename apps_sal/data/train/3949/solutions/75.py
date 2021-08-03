import math


def calculate_tip(amount, rating):
    if rating.lower() == 'poor':
        return math.ceil((amount / 100) * 5)
    elif rating.lower() == 'good':
        return math.ceil((amount / 100) * 10)
    elif rating.lower() == 'great':
        return math.ceil((amount / 100) * 15)
    elif rating.lower() == 'excellent':
        return math.ceil((amount / 100) * 20)
    elif rating.lower() not in ['poor', 'good', 'great', 'excellent', 'terrible']:
        return 'Rating not recognised'
    else:
        return 0
