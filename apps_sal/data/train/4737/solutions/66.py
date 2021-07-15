def fuel_price(litres, price):
    if litres < 2:
        return litres * price
    elif litres < 4:
        return litres * (price - .05) 
    elif litres < 6:
        return litres * (price - 0.1)
    elif litres < 8:
        return litres * (price - 0.15)
    elif litres < 10:
        return litres * (price - 0.20)
    else:
        return litres * (price - 0.25)
