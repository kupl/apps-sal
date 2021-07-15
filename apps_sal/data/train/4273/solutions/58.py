def shorten_to_date(long_date):
    if long_date[-4] in '123456789': return long_date[0:-6]
    else: return long_date[0:-5]
