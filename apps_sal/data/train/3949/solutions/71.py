import math
def calculate_tip(amount, rating):
    """(^-__-^)"""
    dic = {"terrible": 0, "poor": 5, "good": 10, "great": 15, "excellent": 20}
    return math.ceil((amount / 100) * dic.get(rating.lower())) if rating.lower() in dic else 'Rating not recognised'

