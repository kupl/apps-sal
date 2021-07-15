def shorten_to_date(long_date):
    f = long_date.find(', ')
    return long_date[: f]

