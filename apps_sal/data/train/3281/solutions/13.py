def unlucky_days(year):
    import datetime
    (i, count) = (1, 0)
    while i <= 12:
        if datetime.datetime(year, i, 13).strftime('%w') == '5':
            count += 1
        i += 1
    return count
