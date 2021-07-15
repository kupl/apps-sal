def shorten_to_date(long_date):
    l=([x.strip(',') for x in long_date.split(',')])
    del l[-1]
    return (' ').join(l)
