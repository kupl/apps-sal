def calculate_tip(amount, rating):
    import math
    table = {
        "terrible": 0,
        "poor": 0.05,
        "good": .1,
        "great": 0.15,
        "excellent": .2
    }
    rating = rating.lower()
    if rating in table:
        return(math.ceil(amount * table[rating]))
    else:
        return("Rating not recognised")
