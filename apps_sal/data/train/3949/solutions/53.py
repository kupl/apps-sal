from math import ceil


def calculate_tip(amount, rating):
    per = {
        "terrible": 0,
        "poor": 0.05,
        "good": 0.1,
        "great": 0.15,
        "excellent": 0.2
    }.get(rating.lower(), None)

    return ceil(amount * per) if per != None else 'Rating not recognised'
