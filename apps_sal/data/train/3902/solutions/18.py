from math import floor

def duty_free(price: int, discount: int, holiday_cost: int) -> int:
    """
    How many bottles of duty free whiskey you would have to buy such that the saving 
    over the normal high street price would effectively cover the cost of your holiday?
    """
    return floor(holiday_cost / (price * (discount / 100)))
