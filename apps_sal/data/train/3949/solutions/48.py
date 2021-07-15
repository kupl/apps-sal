import math

def calculate_tip(amount, rating):
    case = {
        'terrible' : 0,
        'poor' : .05,
        'good' : .1,
        'great' : .15,
        'excellent' : .2,
    }    
    return 'Rating not recognised' if rating.lower() not in case else math.ceil(amount * case.get(rating.lower()))
