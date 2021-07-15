def mango(quantity, price):
    groups_three = quantity // 3
    extra = quantity % 3
    cost = 0
    cost = cost + groups_three * (price * 2)
    cost = cost + extra * price
    return cost
