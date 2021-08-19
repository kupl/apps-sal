import datetime


def unlucky_days(year):
    date_ = datetime.date(year, 1, 1)
    while date_.weekday() != 4:
        date_ += datetime.timedelta(days=1)
    bad_days = 0
    while date_.year == year:
        if date_.day == 13:
            bad_days += 1
        date_ += datetime.timedelta(days=7)
    return bad_days
