from math import ceil


def calculate_tip(amount, rating):
    if rating.lower() == 'terrible':
        return ceil(amount * 0)
    elif rating.lower() == 'poor':
        return ceil(amount * 0.05)
    elif rating.lower() == 'good':
        return ceil(amount * 0.1)
    elif rating.lower() == 'great':
        return ceil(amount * 0.15)
    elif rating.lower() == 'excellent':
        return ceil(amount * 0.2)
    else:
        return 'Rating not recognised'
