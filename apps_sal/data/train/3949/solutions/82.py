from math import ceil


def calculate_tip(amount, rating):
    return {'terrible': 0, 'poor': ceil(amount * (0.05)), 'good': ceil(amount * (1 / 10)), 'great': ceil(amount * (15 / 100)), 'excellent': ceil(amount * (1 / 5))}.get(rating.lower(), 'Rating not recognised')
