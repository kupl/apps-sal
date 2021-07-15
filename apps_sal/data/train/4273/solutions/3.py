def shorten_to_date(long_date):
    index = long_date.index(',')
    new_string = long_date[:index]
    return (new_string)
