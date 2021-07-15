import math

def calculate_tip(amount, rating):
    factor = 0
    rating = rating.lower()
    if (rating == "terrible"):
        pass
    elif (rating == "poor"):
        factor = 0.05
    elif (rating == "good"):
        factor = 0.1
    elif (rating == "great"):
        factor = 0.15
    elif (rating == "excellent"):
        factor = 0.2
    else:
        return 'Rating not recognised'
    return math.ceil(amount * factor)
