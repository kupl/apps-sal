def shorten_to_date(long_date):
    for i in range(len(long_date)):
        if long_date[i] == ',':
            return long_date[:i]
    return long_date
