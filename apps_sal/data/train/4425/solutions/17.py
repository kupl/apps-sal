def mango(quantity, price):
    groups_of_three = quantity // 3
    remainding = quantity % 3
    return groups_of_three * 2 * price + remainding * price
