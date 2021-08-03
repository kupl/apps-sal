def shorten_to_date(long_date):
    x = ""
    for i in long_date:
        if i != ",":
            x += i
        else:
            break
    return x
