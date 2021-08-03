import calendar


def unlucky_days(year):
    f13 = 0
    for i in range(1, 13):
        c = calendar.monthcalendar(year, i)
        for f in [c[0], c[1], c[2], c[3]]:
            if f[calendar.FRIDAY] == 13:
                f13 += 1
    return f13
