def shorten_to_date(long_date):
    a = len(long_date) - long_date.index(',')
    return long_date[:-a]
