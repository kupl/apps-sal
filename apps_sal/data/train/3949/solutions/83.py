from math import ceil


def calculate_tip(amount, rating):
    dict = {'Terrible': 0, 'Poor': 0.05, 'Good': 0.1, 'Great': 0.15, 'Excellent': 0.2}
    return ceil(amount * dict.get(rating.capitalize())) if dict.get(rating.capitalize(), 'nothing') != 'nothing' else 'Rating not recognised'
