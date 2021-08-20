import math
tip = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}


def calculate_tip(amount, rating):
    rating = rating.lower()
    if rating not in tip:
        return 'Rating not recognised'
    return math.ceil(amount * tip[rating])
