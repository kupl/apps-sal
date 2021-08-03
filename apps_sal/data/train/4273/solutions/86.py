def shorten_to_date(long_date):
    new_date = long_date.partition(",")
    return new_date[0]
