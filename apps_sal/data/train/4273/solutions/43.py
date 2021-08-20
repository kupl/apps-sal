def shorten_to_date(long_date):
    date = long_date.split()
    actual = str(date[0] + ' ' + date[1] + ' ' + date[2])
    actual = actual.replace(',', '')
    return actual
