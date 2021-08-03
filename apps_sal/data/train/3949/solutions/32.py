import math


def calculate_tip(amount, rating):
    bruh = {
        'terrible': 0,
        'poor': math.ceil(amount * .05),
        'good': math.ceil(amount * .1),
        'great': math.ceil(amount * .15),
        'excellent': math.ceil(amount * .2)
    }
    sobaka = rating.lower()
    return bruh.get(sobaka) if sobaka in bruh.keys() else 'Rating not recognised'
