def to_currency(price):
    p = str(price)
    return p if len(p) <= 3 else to_currency(p[:-3]) + ',' + p[-3:]
