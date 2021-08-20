import re
_24H = re.compile('^([01]?\\d|2[0-3]):[0-5]\\d$')


def validate_time(time):
    return bool(_24H.match(time))
