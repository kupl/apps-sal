import re


def date_checker(date):
    return bool(re.match('\\d{2}-\\d{2}-\\d{4} \\d{2}:\\d{2}', date))
