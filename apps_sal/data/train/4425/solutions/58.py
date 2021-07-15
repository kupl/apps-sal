def mango(quantity, price):
    if quantity % 3 == 0:
        a = (quantity / 3) * 2
        return a * price
    elif quantity % 3 != 0:
        b = quantity % 3
        c = ((quantity - b) / 3) * 2
        d = (c + b) 
        return d * price

