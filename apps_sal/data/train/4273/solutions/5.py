def shorten_to_date(long_date):
    #your code here
    num = long_date.find(',')
    return long_date[0:num]
