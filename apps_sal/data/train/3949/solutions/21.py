import math


def calculate_tip(amount, rating):
    ratings = {
        "Terrible": 0,
        "Poor": .05,
        "Good": .10,
        "Great": .15,
        "Excellent": .20
    }

    try:
        return math.ceil(amount * ratings.get(rating.title()))
    except:
        return "Rating not recognised"
