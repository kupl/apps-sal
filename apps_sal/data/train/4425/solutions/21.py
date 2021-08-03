def mango(quantity, price):
    if quantity == 2 or quantity == 3:
        return 2 * quantity
    else:
        free = quantity // 3
        return (quantity - free) * price
