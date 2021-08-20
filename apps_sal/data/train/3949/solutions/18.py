import math


def calculate_tip(amount, rating):
    tipTypes = ['terrible', 'poor', 'good', 'great', 'excellent']
    if rating.lower() in tipTypes:
        return math.ceil(amount * tipTypes.index(rating.lower()) * 0.05)
    else:
        return 'Rating not recognised'
