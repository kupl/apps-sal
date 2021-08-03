import datetime


def unlucky_days(y):  # (year,month,day)
    return len([i for i in range(12) if datetime.date(y, i + 1, 13).weekday() == 4])
    # for month the range of 12 months,
    # if the weekday == friday 13th in y year, i+1 month,
    # return the number of months that have friday the 13th in them as a list.
    # find the length of it.
