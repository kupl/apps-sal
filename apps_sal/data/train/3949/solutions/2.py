import math


def calculate_tip(amount, rating):
    rating = rating.lower()
    tip = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}.get(rating)
    if tip == None:
        return 'Rating not recognised'
    return int(math.ceil(amount * tip))
