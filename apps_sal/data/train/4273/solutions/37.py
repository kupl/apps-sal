def shorten_to_date(long_date):
    for i in range(-6, -3):
        if long_date[i] == ",":
            return long_date[:i]
