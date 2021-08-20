from math import ceil


def calculate_tip(amount, rating):
    service = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    tip = service.get(rating.lower(), 'Rating not recognised')
    return tip if isinstance(tip, str) else ceil(tip * amount)
