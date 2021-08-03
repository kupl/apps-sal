import re


def shorten_to_date(long_date):
    return re.sub(', [0-9]{1,2}(a|p)m', '', long_date)
