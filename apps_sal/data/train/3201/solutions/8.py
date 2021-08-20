import re


def validate_time(time):
    pattern = re.compile('^[012]?((?<=2)[0-3]|(?<!2)[0-9]):[0-5][0-9]$')
    return bool(re.fullmatch(pattern, time))
