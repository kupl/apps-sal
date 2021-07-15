def adjust(coin, price):
    return price / coin * coin + bool(price % coin) * coin
