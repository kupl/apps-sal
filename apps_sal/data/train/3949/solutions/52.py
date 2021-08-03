import math
dict = {
    "terrible": 0.0,
    "poor": 0.05,
    "good": 0.1,
    "great": 0.15,
    "excellent": 0.2
}


def calculate_tip(amount, rating):
    try:
        return math.ceil(float(amount) * dict[rating.lower()])
    except:
        return 'Rating not recognised'
