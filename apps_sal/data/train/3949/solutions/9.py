from math import ceil


def calculate_tip(amount, rating):
    tip = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    return ceil(amount * tip[rating.lower()]) if rating.lower() in tip else 'Rating not recognised'
