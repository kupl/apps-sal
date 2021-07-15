from datetime import timedelta

def past(h, m, s):
    return timedelta(hours=h, minutes=m, seconds=s) // timedelta(milliseconds=1)
