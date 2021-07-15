def shorten_to_date(date):
    date = date.replace(',','').split(' ')
    return date[0] + ' ' + date[1] + ' ' + date[2]
