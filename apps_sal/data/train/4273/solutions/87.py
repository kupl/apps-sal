def shorten_to_date(long_date):
    #your code here
    g = long_date.rfind(',')
    return long_date[0:g]
