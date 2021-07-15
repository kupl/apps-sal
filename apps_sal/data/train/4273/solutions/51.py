def shorten_to_date(long_date):
    string = str(long_date)
    string = string.replace(',','')
    string = string.split(' ')
    string.pop()
    string = ' '.join(string)
    return string
