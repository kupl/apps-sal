from math import ceil


def calculate_tip(amount, rating):
    tips = {
        'terrible': 0,
        'poor': .05,
        'good': .1,
        'great': .15,
        'excellent': .2
    }
    if rating.lower() in tips:
        return ceil(amount * tips[rating.lower()])
    else:
        return 'Rating not recognised'
