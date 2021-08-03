import math


def calculate_tip(amount, rating):
    str_rating = rating.lower()

    dict = {
        'terrible': 0,
        'poor': 5,
        'good': 10,
        'great': 15,
        'excellent': 20

    }
    if str_rating in dict:
        result = ((amount * dict[str_rating]) / 100)
        return math.ceil(result)
    else:
        return "Rating not recognised"
