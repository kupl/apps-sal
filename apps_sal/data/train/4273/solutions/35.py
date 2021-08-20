def shorten_to_date(long_date):
    return ' '.join([i.replace(',', '') for i in long_date.split()[:-1]])
