import math


def calculate_tip(amount, rating):
    rating = rating.lower()
    if rating == "poor":
        return math.ceil(amount * 0.05)
    elif rating == "good":
        return math.ceil(amount * 0.1)
    elif rating == "great":
        return math.ceil(amount * 0.15)
    elif rating == "excellent":
        return math.ceil(amount * 0.2)
    elif rating == "terrible":
        return math.ceil(amount * 0)
    else:
        return "Rating not recognised"
