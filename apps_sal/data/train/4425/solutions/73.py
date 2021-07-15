def mango(quantity, price):
    total = 0
    for i in range(1, quantity + 1):
        if i % 3 != 0:
            total += price
        else:
            pass
    return total
