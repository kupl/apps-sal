import re


def date_checker(date):
    return bool(re.match('(\\d\\d-){2}\\d{4}\\s\\d\\d:\\d\\d', date))
