def shorten_to_date(long_date):
    date_list = long_date.split(" ")
    del date_list[-1]
    short_date = " ".join(date_list)
    short_date = short_date[:-1]
    return short_date

