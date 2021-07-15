def shorten_to_date(long_date):
    return ' '.join(long_date.split()[:-1]).replace(',', '')
