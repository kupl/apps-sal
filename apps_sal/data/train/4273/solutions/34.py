import re


def shorten_to_date(long_date):
    match_date = re.search('\w*\s\w*\s\d*', long_date)
    return match_date.group(0)
