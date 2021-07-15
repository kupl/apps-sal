def mango(quantity, price):
    if quantity / 3 == 1:
        return (quantity - 1) * price 
    else:
        actual_quantity = quantity // 3
        return (quantity - actual_quantity) * price
