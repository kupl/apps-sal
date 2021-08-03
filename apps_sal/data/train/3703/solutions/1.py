def order(pizzas, salads, appetizers):
    side_total = 0
    pizza_total = 0
    side_total += salads * 3
    side_total += appetizers * 5
    pizza_total += pizzas * 1.5
    if pizza_total <= 10:
        pizza_total += 10
    elif pizza_total >= 10:
        pizza_total += 10 * 2
    return max(side_total, pizza_total)
