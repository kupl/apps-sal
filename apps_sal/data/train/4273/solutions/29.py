def shorten_to_date(long_date):
    index = long_date.find(',')
    return long_date[0:index]
