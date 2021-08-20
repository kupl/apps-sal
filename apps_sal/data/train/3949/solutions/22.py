import math


def calculate_tip(amount, rating):
    rating = rating.lower()
    if rating == 'terrible':
        terrible = int(amount) * 0
        terrible = math.ceil(terrible)
        return terrible
    elif rating == 'poor':
        poor = int(amount) * 0.05
        poor = math.ceil(poor)
        return poor
    elif rating == 'good':
        good = int(amount) * 0.1
        good = math.ceil(good)
        return good
    elif rating == 'great':
        great = int(amount) * 0.15
        great = math.ceil(great)
        return great
    elif rating == 'excellent':
        excellent = int(amount) * 0.2
        excellent = math.ceil(excellent)
        return excellent
    else:
        return 'Rating not recognised'
