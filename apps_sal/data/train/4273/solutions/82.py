def shorten_to_date(long_date):
    return long_date.replace(long_date[long_date.index(','):], '')
