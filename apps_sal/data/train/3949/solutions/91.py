import math
def calculate_tip(amount, rating):
    amount = math.ceil(amount)
    if rating.title() == 'Terrible':
        return amount * 0
    elif rating.title() == 'Poor':
        return math.ceil(amount * 0.05)
    elif rating.title() == 'Good':
        return math.ceil(amount * 0.10)
    elif rating.title() == 'Great':
        return math.ceil(amount * 0.15)
    elif rating.title() == 'Excellent':
        return math.ceil(amount * 0.2)
    else:
        return 'Rating not recognised'
