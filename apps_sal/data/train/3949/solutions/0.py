from math import ceil


def calculate_tip(amount, rating):
    tips = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    if rating.lower() in tips:
        return ceil(amount * tips[rating.lower()])
    else:
        return 'Rating not recognised'
