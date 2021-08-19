def order(pizzas, salads, appetizers):
    time = 0
    if pizzas > 0:
        time = pizzas * 3 / 2
        oven_cycles = pizzas // 10 + 1
        time = time + oven_cycles * 10
        time_2 = salads * 3 + appetizers * 5
        if time > time_2:
            return time
        else:
            return time_2
    else:
        time_2 = salads * 3 + appetizers * 5
        return time_2
