import math

def order(pizzas, salads, appetizers):
    pizza_prep = 3 * pizzas / 2
    pizza_cook = math.ceil(pizzas / 10) * 10
    salad_prep = salads * 3
    app_prep = appetizers * 5
    return max([pizza_prep + pizza_cook, salad_prep + app_prep])
