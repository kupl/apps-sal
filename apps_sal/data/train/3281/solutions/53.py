import datetime


def unlucky_days(year):
    count = 0
    for i in range(1, 13):
        a = datetime.datetime(year, i, 13)
        if a.strftime('%A') == 'Friday':
            count += 1
    return count
