def mango(total_quantity, price_per_mango):

    quantity_of_set_3 = int(total_quantity / 3)
    remaining_mangoes = total_quantity % 3

    price_per_two_mangoes = price_per_mango * 2
    cost_of_set3 = quantity_of_set_3 * price_per_two_mangoes

    cost_remaining_mangoes = remaining_mangoes * price_per_mango
    total_cost = cost_of_set3 + cost_remaining_mangoes

    return total_cost
