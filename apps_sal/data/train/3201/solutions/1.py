import re


def validate_time(timestamp):
    return bool(re.match('(2[0-3]|[01]?\\d):[0-5]\\d$', timestamp))
