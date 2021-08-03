def to_currency(price):
    p = str(price)[::-1]
    return ",".join(p[i:i + 3] for i in range(0, len(p), 3))[::-1]
