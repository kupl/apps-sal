from math import ceil
RATES = (('terrible', 0), ('poor', 0.05), ('good', 0.1), ('great', 0.15), ('excellent', 0.2))


def calculate_tip(amount, rating):
    return {name: ceil(rate * amount) for (name, rate) in RATES}.get(rating.lower(), 'Rating not recognised')
