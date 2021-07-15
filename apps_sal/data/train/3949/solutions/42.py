import math

def calculate_tip(amount, rating):
    tips = {'terrible': 0, 'poor': 5, 'good': 10, 'great': 15, 'excellent': 20}
    return math.ceil(tips[rating.lower()] / 100.0 * amount) if rating.lower() in tips else 'Rating not recognised'
