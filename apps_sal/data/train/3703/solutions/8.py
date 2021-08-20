def order(pizzas, salads, appetizers):
    pizza_time = 3 * pizzas / 2 + 10 * (pizzas // 10 + 1)
    salad_app_time = 3 * salads + 5 * appetizers
    return max(pizza_time, salad_app_time)
