def shorten_to_date(long_date):
    if long_date.endswith('pm') or long_date.endswith('am'):
        split_long_date = long_date.split(',', 1)
        return split_long_date[0]
