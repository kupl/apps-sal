from calendar import weekday


def unlucky_days(year):
    c = 0
    for m in range(1, 13):
        u = weekday(year, m, 13)
        if u == 4:
            c += 1
    return c
