def shorten_to_date(long_date):
    string = ""
    for c in long_date:
        if c != ",":
            string += c
        else:
            return string
