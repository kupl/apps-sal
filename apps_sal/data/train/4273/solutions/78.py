def shorten_to_date(long_date):
    short=''
    for i in long_date:
        if i==",":
            break
        short+=i
    return short
