from datetime import timedelta


def past(h, m, s):
    d = timedelta(hours=h, minutes=m, seconds=s)
    return d.seconds * 1000
