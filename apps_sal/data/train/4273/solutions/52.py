def shorten_to_date(long_date):
    ld = long_date
    ind = ld.index(',')
    return ld[:ind]
