import re


def validate_time(s):
    return bool(re.match('([01]?\\d|2[0-3]):[0-5]\\d$', s))
