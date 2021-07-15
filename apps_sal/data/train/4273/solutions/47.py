def shorten_to_date(long_date):
    long_date = long_date.replace(',', '')
    long_date = long_date.split(" ")
    del long_date[3]
    long_date = " ".join(long_date)
    return long_date

print(shorten_to_date("Monday February 2, 8pm"))
