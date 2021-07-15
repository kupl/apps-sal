def shorten_to_date(long_date):
    counter = 0
    for i in long_date:
        if i == ",":
            counter = long_date.find(i)
    return long_date[:counter]
