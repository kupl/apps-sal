def shorten_to_date(long_date):
    a = long_date.split(', ')
    b = ''.join(a[:-1])
    return b
