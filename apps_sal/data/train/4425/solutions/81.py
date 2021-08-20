def mango(quantity, price):
    total = 0
    for count in range(1, quantity + 1):
        if count % 3 == 0:
            continue
        total += price
    return total
