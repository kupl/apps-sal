from datetime import datetime


def day(date):
    return format(datetime.strptime(date, '%Y%m%d'), '%A')
