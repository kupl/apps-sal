def adjust(coin, price):
    if price % coin == 0:
        return price
    else:
        return (price // coin + 1) * coin
