def adjust(coin, price):
    if(price % coin != 0):
        price += coin - price % coin

    return price
