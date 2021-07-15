import math

def calculate_tip(amount, rating):
    tips = {"terrible" : 0,
            "poor"     : 0.05,
            "good"     : 0.1,
            "great"    : 0.15,
            "excellent": 0.2}.get(rating.lower(), None)
    return math.ceil(amount * tips) if tips is not None else 'Rating not recognised'

