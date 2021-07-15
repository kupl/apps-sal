from math import ceil
def calculate_tip(amount, rating):
    return {
        'terrible': 0,
        'poor': ceil(amount * 0.05),
        'good': ceil(amount * 0.1),
        'great': ceil(amount * 0.15),
        'excellent': ceil(amount * 0.2)}.get(rating.lower(), 'Rating not recognised')
