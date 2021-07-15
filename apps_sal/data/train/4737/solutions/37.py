def fuel_price(litres, price):
    if litres <2:
        return round(litres * price, 2)
    elif litres <4:
        return round(litres * (price-0.05),2)
    elif litres <6:
        return round(litres * (price-0.1),2)
    elif litres <8:
        return round(litres * (price-0.15),2)
    elif litres <10:
        return round(litres * (price-0.2),2)
    else:
        return round(litres * (price-0.25),2)
