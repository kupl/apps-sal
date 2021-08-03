def unlucky_days(year):
    from datetime import datetime as dt
    from datetime import timedelta

    cnt = 0
    x = dt(year, 1, 1)
    while x.year == year:
        x = x + timedelta(days=1)
        if x.day == 13 and x.weekday() == 4:
            cnt = cnt + 1
    return cnt
