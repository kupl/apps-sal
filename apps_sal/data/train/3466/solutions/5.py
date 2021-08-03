import re


def date_checker(date):
    return True if re.match(r"\d{2}-\d{2}-\d{4} \d{2}:\d{2}", date) else False
