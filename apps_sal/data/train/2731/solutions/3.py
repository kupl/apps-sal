from datetime import datetime, timedelta


def day_and_time(mins):
    d = datetime.strptime('2019-01-13 00:00', '%Y-%m-%d %H:%M') + timedelta(minutes=mins)
    return d.strftime('%A %H:%M')
