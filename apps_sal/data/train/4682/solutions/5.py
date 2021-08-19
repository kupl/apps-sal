def date_correct(date):
    if date in ('', 0, None):
        return date
    from re import findall
    date = findall('\\A(\\d{2})\\.(\\d{2})\\.(\\d{4})\\Z', date)
    if len(date) == 0:
        return None
    import datetime
    date = [int(x) for x in date[0][::-1]]
    date[0] += (date[1] - 1) // 12
    date[1] = (date[1] - 1) % 12 + 1
    newdate = datetime.date(date[0], date[1], 1)
    newdate += datetime.timedelta(days=date[2] - 1)
    return '{0:02d}.{1:02d}.{2}'.format(newdate.day, newdate.month, newdate.year)
