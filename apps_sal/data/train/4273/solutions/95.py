def shorten_to_date(long_date):
    sep = ','
    return sep.join(long_date.split(sep)[:-1])
