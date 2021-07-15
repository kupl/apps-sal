def shorten_to_date(long_date):
    a = long_date.split(",")
    x = list(a)
    return(' '.join(x[:-2] + x[:-1]))
