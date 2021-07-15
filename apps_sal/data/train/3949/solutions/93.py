import math

def calculate_tip(amount, rating):
    rate = rating.lower()
    
    discount = 0
    discountTwo = amount * .05
    discountThree = amount * .10
    discountFour = amount * .15
    discountFive = amount * .20
    
    if rate == "terrible":
        return math.ceil(discount)
    elif rate == "poor":
        return math.ceil(discountTwo)
    elif rate == "good":
        return math.ceil(discountThree)
    elif rate == "great":
        return math.ceil(discountFour)
    elif rate == "excellent":
        return math.ceil(discountFive)
    return "Rating not recognised"
