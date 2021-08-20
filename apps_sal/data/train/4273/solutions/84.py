import re


def shorten_to_date(long_date):
    return re.sub(',\\s\\d\\w.+', '', long_date)
