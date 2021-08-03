def to_currency(price):
    price = str(price)[::-1]
    x = [price[i:i + 3] for i in range(0, len(price), 3)]
    return ",".join(x)[::-1]
