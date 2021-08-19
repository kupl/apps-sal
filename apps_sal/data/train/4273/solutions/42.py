def shorten_to_date(long_date):
    comma = long_date.find(',')
    return long_date[0:comma]
