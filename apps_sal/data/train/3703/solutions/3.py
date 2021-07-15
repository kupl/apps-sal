import math

def order(pizzas, salads, appetizers):
    return max(pizzas * 1.5 + math.ceil(pizzas / 10)*10, salads * 3 + appetizers * 5)
