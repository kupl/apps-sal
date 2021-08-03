import numpy as np

d = {
    'Terrible': 0,
    'Poor': 0.05,
    'Good': 0.1,
    'Great': 0.15,
    'Excellent': 0.2
}


def calculate_tip(amount, rating):
    try:
        return np.ceil(amount * d[rating.title()])
    except:
        return "Rating not recognised"
