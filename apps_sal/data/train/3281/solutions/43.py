import calendar

def unlucky_days(year):
    res_date = calendar.Calendar()
    res_days = 0
    for month in range(1, 13):
        for day in res_date.itermonthdays2(year, month):
            if day[0] == 13 and day[1] == 4:
                res_days += 1
    return res_days

