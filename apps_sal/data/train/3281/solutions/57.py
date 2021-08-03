from calendar import Calendar


def unlucky_days(year):
    x = Calendar()
    lst = []
    for month in range(1, 13):
        for days in x.itermonthdays2(year, month):
            if days[0] == 13 and days[1] == 4:
                lst.append(days)
    return len(lst)
