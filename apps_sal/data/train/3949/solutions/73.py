from math import ceil


def calculate_tip(amount, rating):
    percent = {"terrible": 0, "poor": 5, "good": 10, "great": 15, "excellent": 20}
    tip = percent.get(rating.lower())
    try:
        return ceil(amount * tip / 100)
    except:
        return "Rating not recognised"
