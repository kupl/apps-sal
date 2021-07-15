def shorten_to_date(long_date):
    end = long_date.index(',')
    return long_date[:end]
