from math import ceil


def calculate_tip(amount, rating):
    ratings = ['terrible', 'poor', 'good', 'great', 'excellent']
    if rating.lower() in ratings:
        tip = 5 * ratings.index(rating.lower())
        return ceil(tip / 100 * amount)
    else:
        return 'Rating not recognised'
