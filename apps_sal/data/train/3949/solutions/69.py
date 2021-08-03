import math


def calculate_tip(amount, rating):
    dict = {"terrible": 0, "poor": 0.05, "good": 0.10, "great": 0.15, "excellent": 0.20}
    return math.ceil(amount * dict[rating.lower()]) if rating.lower() in dict else "Rating not recognised"
