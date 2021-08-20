import datetime


def unlucky_days(year):
    ans = 0
    for i in range(1, 13):
        day = datetime.date(year, i, 13)
        ans += day.weekday() == 4
    return ans
