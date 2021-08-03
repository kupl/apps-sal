from math import ceil


def calculate_tip(amount, rating):
    tab = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    mpl = tab.get(rating.lower(), -1)
    return ceil(amount * mpl) if mpl >= 0 else "Rating not recognised"
