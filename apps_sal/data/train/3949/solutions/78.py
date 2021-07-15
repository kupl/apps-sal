from math import ceil

def calculate_tip(amount, rating):
    tip = ceil(amount * {"terrible": 0, "poor": 0.05, "good": 0.1, "great": 0.15, "excellent": 0.20}.get(rating.lower(), -1))
    return tip if tip >= 0 else "Rating not recognised"
