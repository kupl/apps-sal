import re


def validate_time(time):
    return bool(re.findall('^([01]?[0-9]|2[0-3]):[0-5][0-9]$', time))
