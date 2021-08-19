from math import ceil


def calculate_tip(amount, rating):
    ratings = {'terrible': 0, 'poor': 5, 'good': 10, 'great': 15, 'excellent': 20}
    if rating.lower() not in ratings.keys():
        return 'Rating not recognised'
    return ceil(ratings.get(rating.lower()) * amount / 100)
