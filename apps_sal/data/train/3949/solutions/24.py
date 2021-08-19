import math


def calculate_tip(amount, rating):
    service_perc = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    try:
        return math.ceil(amount * service_perc[rating.lower()])
    except KeyError:
        return 'Rating not recognised'
