import math


def calculate_tip(amount, rating):
    ratings_dict = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    if rating.lower() not in ratings_dict.keys():
        return 'Rating not recognised'
    else:
        return math.ceil(ratings_dict.get(rating.lower()) * amount)
