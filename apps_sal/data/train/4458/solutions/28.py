from re import match
from time import strftime
from time import gmtime


def time_correct(t):
    if not t:
        return t
    if not match('\\d{2}:\\d{2}:\\d{2}', t):
        return None
    (hrs, mnt, sec) = [int(x) for x in t.split(':')]
    total = hrs * 3600 + mnt * 60 + sec
    return strftime('%H:%M:%S', gmtime(total))
