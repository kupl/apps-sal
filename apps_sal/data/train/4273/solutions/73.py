def shorten_to_date(long_date):
    shorten = ''
    for i in long_date:
        if i == ',':
            break
        shorten += i
    return shorten
