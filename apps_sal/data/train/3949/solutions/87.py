import math

def calculate_tip(amount, rating):
    x = {
        'terrible': 0,
        'poor': 5,
        'good': 10,
        'great': 15,
        'excellent': 20
    }.get(rating.lower())
    return math.ceil(x * amount/100) if x != None else 'Rating not recognised'
