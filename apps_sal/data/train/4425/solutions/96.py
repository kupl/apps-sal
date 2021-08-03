def mango(quantity, price):
    sum = 0

    while quantity > 2:
        quantity = quantity - 3
        sum = sum + price * 2

    return sum + price * quantity
