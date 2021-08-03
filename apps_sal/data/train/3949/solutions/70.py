import math


def calculate_tip(amount, rating):
    if(rating.lower() == "poor".lower()):
        a = amount * (5 / 100)
        return math.ceil(a)
    elif(rating.lower() == "Excellent".lower()):
        a = amount * (20 / 100)
        return math.ceil(a)
    elif(rating.lower() == "Great".lower()):
        a = amount * (15 / 100)
        return math.ceil(a)
    elif(rating.lower() == "Good".lower()):
        a = amount * (10 / 100)
        return math.ceil(a)
    elif(rating.lower() == "terrible".lower()):
        return 0
    else:
        return "Rating not recognised"
