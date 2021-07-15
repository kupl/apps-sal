import math
def calculate_tip(amount, rating):
    rates = {'terrible': 0, 'poor': 0.05, 'good': 0.1, 'great': 0.15, 'excellent':0.2}
    if rating.lower() not in rates:
        return "Rating not recognised"
    else:
        return math.ceil(amount * rates[rating.lower()])
