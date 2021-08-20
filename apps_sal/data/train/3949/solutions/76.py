import math


def calculate_tip(amount, rating):
    tip = {'Terrible': 0, 'Poor': 5 / 100, 'Good': 10 / 100, 'Great': 15 / 100, 'Excellent': 20 / 100}
    try:
        return math.ceil(int(amount) * tip[rating.title()])
    except:
        return 'Rating not recognised'
