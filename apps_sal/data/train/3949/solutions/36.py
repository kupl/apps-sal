from math import ceil

RATES = ('terrible', 'poor', 'good', 'great', 'excellent')


def calculate_tip(amount, rating):
    return {name: ceil(rate * amount * .05) for rate, name in enumerate(RATES)}.get(rating.lower(), "Rating not recognised")
