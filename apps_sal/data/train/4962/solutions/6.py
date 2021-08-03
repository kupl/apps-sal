import datetime


def days_until_christmas(year):

    k = year.year

    dc = datetime.date(k, 12, 25)
    r = dc - year

    ret = r.days

    if ret >= 0:
        return ret
    else:
        dc = datetime.date(k + 1, 12, 25)
        r = dc - year

        ret = r.days

        return ret
