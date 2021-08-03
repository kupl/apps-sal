import math


def calculate_tip(amount, rating):
    tip_table = {'terrible': 0,
                 'poor': 0.05,
                 'good': 0.10,
                 'great': 0.15,
                 'excellent': 0.20}
    rating = rating.lower()
    if rating in tip_table:
        return math.ceil(amount * tip_table[rating.lower()])
    else:
        return "Rating not recognised"
