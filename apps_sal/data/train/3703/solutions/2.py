def order(pizzas, salads, appetizers):  
    pizza_time = 3 * (pizzas / 2) + 10 * ((pizzas // 11) + 1)
    other_time = 3 * salads + 5 * appetizers

    return max(other_time, pizza_time)
