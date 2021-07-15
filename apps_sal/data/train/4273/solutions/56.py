def shorten_to_date(long_date):
    a = long_date.find(",")
    b = long_date[0:a]
    return b
