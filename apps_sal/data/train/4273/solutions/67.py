def shorten_to_date(long_date):
    short_date=long_date.replace(",", "").split(" ")
    short_date.pop()
    return " ".join(short_date)
