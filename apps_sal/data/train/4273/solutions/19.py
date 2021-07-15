def shorten_to_date(long_date):
    x = long_date.split(',')
    del x[-1]
    return x[0]

