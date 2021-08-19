def shorten_to_date(long_date):
    g = long_date.rfind(',')
    return long_date[0:g]
