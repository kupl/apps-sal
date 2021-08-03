def mango(quantity, price):
    free = 0
    for i in range(1, quantity + 1):
        if i % 3 == 0:
            free += 1
    return price * (quantity - free)
