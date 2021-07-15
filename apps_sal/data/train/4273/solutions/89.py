def shorten_to_date(long_date):
    x = long_date.split(',')
    shortened = x[:1]
    emptystring = ''
    for eachchar in shortened:
        emptystring = emptystring + eachchar
    return emptystring

