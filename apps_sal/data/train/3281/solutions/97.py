import calendar


def unlucky_days(year):
    c = 0
    cal = calendar.Calendar()
    for i in range(1, 13):
        for d, w in cal.itermonthdays2(year, i):
            if d == 13 and w == 4:
                c = c + 1
    return c
