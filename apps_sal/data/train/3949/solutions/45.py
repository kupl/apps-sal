import math
d = {

    'terrible': 0,
    'poor': 5,
    'good': 10,
    'great': 15,
    'excellent': 20,
    'bla': 'Rating not recognised'
}


def calculate_tip(amount, rating):
    rating = rating.lower()
    if rating in d.keys():
        return math.ceil((amount * d.get(rating)) / 100)
    else:
        return 'Rating not recognised'
