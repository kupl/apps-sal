from math import ceil


def calculate_tip(amount, rating):
    rating_table = {'Terrible': 0, 'Poor': 0.05, 'Good': 0.1, 'Great': 0.15, 'Excellent': 0.2}
    rating = rating.title()
    if rating in rating_table:
        return ceil(amount * rating_table.get(rating))
    else:
        return 'Rating not recognised'
