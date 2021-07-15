def shorten_to_date(long_date):
    date_split = long_date.split()
    
    date_split_no_time = date_split[:3]
    short_date = ' '.join(date_split_no_time)
    short_date = short_date.replace(",","")
    return short_date
