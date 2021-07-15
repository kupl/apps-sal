from datetime import datetime, timedelta


def day_and_time(mins):
    return format(datetime(2018, 7, 1) + timedelta(minutes=mins), '%A %H:%M')
