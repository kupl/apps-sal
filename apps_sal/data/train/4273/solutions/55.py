def shorten_to_date(long_date):
    sep = long_date.find(',')
    return long_date[:sep]
