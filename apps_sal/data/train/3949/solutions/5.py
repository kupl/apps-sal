from math import ceil
D = {"terrible": 0, "poor": 0.05, "good": 0.1, "great": 0.15, "excellent": 0.2}


def calculate_tip(amount, rating):
    rating = D.get(rating.lower(), None)
    return "Rating not recognised" if rating is None else ceil(amount * rating)
