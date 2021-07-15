import datetime
def past(h, m, s):
    dt = datetime.timedelta(hours=h, minutes=m, seconds=s)
    return 1000 * dt.total_seconds()

