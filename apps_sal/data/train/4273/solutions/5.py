def shorten_to_date(long_date):
    num = long_date.find(',')
    return long_date[0:num]
