def shorten_to_date(long_date):
    pos = 0
    for i in range(len(long_date)):
        pos += 1
        if long_date[i] == ',':
            break
    pos -= 1
    return long_date[:pos]
