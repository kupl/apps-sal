import math


def calculate_tip(amount, rating):
    rate = rating.lower()
    discount = 0
    discountTwo = amount * 0.05
    discountThree = amount * 0.1
    discountFour = amount * 0.15
    discountFive = amount * 0.2
    if rate == 'terrible':
        return math.ceil(discount)
    elif rate == 'poor':
        return math.ceil(discountTwo)
    elif rate == 'good':
        return math.ceil(discountThree)
    elif rate == 'great':
        return math.ceil(discountFour)
    elif rate == 'excellent':
        return math.ceil(discountFive)
    return 'Rating not recognised'
