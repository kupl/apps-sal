def mango(quantity, price):
    priceOfTwo = quantity // 3
    remaining = quantity - priceOfTwo * 3
    return priceOfTwo * price * 2 + remaining * price
