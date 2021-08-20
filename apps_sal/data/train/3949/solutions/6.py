import math
dict = {'terrible': 0, 'poor': 5, 'good': 10, 'great': 15, 'excellent': 20}


def calculate_tip(amount, rating):
    return 'Rating not recognised' if dict.get(rating.lower(), 'null') == 'null' else math.ceil(dict.get(rating.lower(), 'null') / 100 * amount)
