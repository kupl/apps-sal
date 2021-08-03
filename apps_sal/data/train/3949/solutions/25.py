import math


def calculate_tip(amount, rating):
    rating = rating.lower()

    if rating == "terrible":
        return 0
    if rating == "poor":
        return int(math.ceil(amount * .05))
    if rating == "good":
        return int(math.ceil(amount * .1))
    if rating == "great":
        return int(math.ceil(amount * .15))
    if rating == "excellent":
        return int(math.ceil(amount * .2))
    else:
        return "Rating not recognised"
