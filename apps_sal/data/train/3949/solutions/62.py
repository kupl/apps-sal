from math import ceil


def calculate_tip(amount, rating):
    TIP = {'terrible': 0, 'poor': 5, 'good': 10, 'great': 15, 'excellent': 20}.get(rating.lower(), None)
    if TIP == None:
        return 'Rating not recognised'
    return ceil((amount * TIP) / 100)
