from math import ceil
RATES = {'terrible': 0, 'poor': 5, 'good': 10, 'great': 15, 'excellent': 20}


def calculate_tip(amount, rating):
    r = rating.lower()
    return 'Rating not recognised' if r not in RATES else ceil(RATES[r] / 100.0 * amount)
