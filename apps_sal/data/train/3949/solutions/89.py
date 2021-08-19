import math


def calculate_tip(amount, rating):
    d = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    for (key, val) in d.items():
        if key == rating.lower():
            return math.ceil(amount * val)
    return 'Rating not recognised'
