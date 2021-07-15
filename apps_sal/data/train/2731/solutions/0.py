from datetime import timedelta, datetime
def day_and_time(mins):
    return "{:%A %H:%M}".format(datetime(2017, 1, 1) + timedelta(minutes = mins))
