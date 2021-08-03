import math


def calculate_tip(amount, rating):
    ratings = ["terrible", "poor", "good", "great", "excellent"]
    index = ratings.index(rating.lower()) if rating.lower() in ratings else -1
    return math.ceil(amount * index * 0.05) if index != -1 else "Rating not recognised"
