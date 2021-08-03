def to_currency(price):
    return ''.join((',' + x[1]) if (x[0] % 3 == 0 and x[0]) else (x[1]) for x in enumerate(str(price)[::-1]))[::-1]
