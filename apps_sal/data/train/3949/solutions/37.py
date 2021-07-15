from math import ceil

RATES = (('terrible', 0), ('poor', .05), ('good', .1), ('great', .15), ('excellent', .2))

def calculate_tip(amount, rating):
    return {name: ceil(rate * amount) for name, rate in RATES}.get(rating.lower(), "Rating not recognised")
