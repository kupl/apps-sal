def shorten_to_date(long_date):
    res = ""
    i = 0
    while long_date[i] != ',':
        res += long_date[i]
        i += 1
    return res
