from math import ceil


def calculate_tip(amount, rating):
    service = {'terrible': 0.0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    return ceil(amount * service[rating.lower()]) if rating.lower() in service.keys() else 'Rating not recognised'
