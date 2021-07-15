def fuel_price(litres, price):
    discount = litres/4 if litres >= 10 else litres * (litres//2 * 5)/100
    return price*litres - discount
