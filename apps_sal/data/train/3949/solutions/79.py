import math


def calculate_tip(amount, rating):
    tips = {'Terrible': 0, 'Poor': 0.05, 'Good': 0.1, 'Great': 0.15, 'Excellent': 0.2}
    return math.ceil(amount * tips[rating.capitalize()]) if rating.capitalize() in tips else 'Rating not recognised'
