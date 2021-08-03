def shorten_to_date(long_date):

    long_date = long_date.rsplit(' ', 1)[0].replace(',', '')
    return long_date
