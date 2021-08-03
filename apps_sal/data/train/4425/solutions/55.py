def mango(quantity, price):
    n = 0
    all_price = 0
    if quantity <= 2:
        return quantity * price
    elif quantity > 2:
        while n < quantity:
            n += 1
            all_price += price
            if n % 3 == 0:
                all_price -= price
    return all_price

    pass
