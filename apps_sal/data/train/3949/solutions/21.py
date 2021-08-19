import math


def calculate_tip(amount, rating):
    ratings = {'Terrible': 0, 'Poor': 0.05, 'Good': 0.1, 'Great': 0.15, 'Excellent': 0.2}
    try:
        return math.ceil(amount * ratings.get(rating.title()))
    except:
        return 'Rating not recognised'
