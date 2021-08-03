import datetime


def day(date):
    yy = int(date[0:4])
    mm = int(date[4:6])
    dd = int(date[6:8])
    return datetime.date(yy, mm, dd).strftime('%A')
