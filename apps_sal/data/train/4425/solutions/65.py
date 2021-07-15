def mango(quantity, price):
    return (int(quantity * 2 / 3) + (1 if quantity % 3 else 0)) * price
