import math


def calculate_tip(amount, rating):
    rating = rating.lower()
    service = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    if rating in service:
        return math.ceil(amount * service[rating])
    else:
        return 'Rating not recognised'
