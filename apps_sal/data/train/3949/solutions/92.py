import numpy as np


def calculate_tip(amount, rating):
    tips = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent': 0.2}
    try:
        return np.ceil(tips[rating.lower()] * amount)
    except:
        return 'Rating not recognised'
