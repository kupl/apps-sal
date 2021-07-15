def shorten_to_date(long_date):
    komma = ','
    string_short = long_date.split(komma, 1)[0]
    return string_short
