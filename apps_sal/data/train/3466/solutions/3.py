import re


def date_checker(date):
    return re.match('(\\d\\d-){2}\\d{4} \\d{2}:\\d{2}', date) != None
