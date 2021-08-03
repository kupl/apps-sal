def shorten_to_date(long_date):
    """condenses extended date into a short one"""
    short_date = ''
    for i in range(len(long_date)):
        if long_date[i] != ",":
            short_date = short_date + long_date[i]
        else:
            break
    print(short_date)
    return short_date
