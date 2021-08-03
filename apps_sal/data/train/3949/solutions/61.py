from math import ceil


def calculate_tip(amount, rating):
    try:
        tip = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}.get(rating.lower())
        return ceil(amount * tip)
    except:
        return 'Rating not recognised'
