def adjust(coin, price):
    return price + (coin - price) % coin
