import math


def calculate_tip(amount, rating):
    tip_table = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    rating = rating.lower()
    if rating in tip_table:
        return math.ceil(amount * tip_table[rating.lower()])
    else:
        return 'Rating not recognised'
