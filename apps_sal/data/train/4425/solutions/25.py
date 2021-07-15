def mango(quantity, price):
    remaining = quantity%3
    quantity = (quantity - remaining) *2/3
    return quantity*price + remaining*price
