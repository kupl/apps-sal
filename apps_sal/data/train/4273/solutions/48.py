def shorten_to_date(long_date):
    return " ".join(list(long_date.split())[0:3]).replace(",", "")
