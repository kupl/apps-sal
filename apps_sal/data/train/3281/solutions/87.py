from datetime import date, timedelta


def unlucky_days(year):
    start_date = date(year, 1, 1)
    end_date = date(year, 12, 31)
    delta_days = (end_date - start_date).days
    count = 0
    for n in range(delta_days):
        if start_date.strftime('%a %d') == 'Fri 13':
            count = count + 1
        start_date = start_date + timedelta(days=1)
    return count
