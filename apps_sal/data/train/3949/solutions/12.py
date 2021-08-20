from collections import defaultdict
from math import ceil
SERVICE = defaultdict(lambda: -1, {'terrible': 0.0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2})


def calculate_tip(amount, rating):
    value = SERVICE[rating.lower()]
    return ceil(amount * value) if value >= 0 else 'Rating not recognised'
