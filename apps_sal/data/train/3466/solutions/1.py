import re


def date_checker(date):
    return bool(re.fullmatch('\\d\\d-\\d\\d-\\d\\d\\d\\d \\d\\d:\\d\\d', date))
