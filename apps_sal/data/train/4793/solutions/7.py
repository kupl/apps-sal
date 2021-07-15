def to_currency(price):
    return '{:,.3f}'.format(price).rstrip('0').rstrip('.')
