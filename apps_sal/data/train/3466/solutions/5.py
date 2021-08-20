import re


def date_checker(date):
    return True if re.match('\\d{2}-\\d{2}-\\d{4} \\d{2}:\\d{2}', date) else False
