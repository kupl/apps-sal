def shorten_to_date(d):
    s = ''
    for i in d:
        if i == ',':
            break
        else:
            s += i
    return s
