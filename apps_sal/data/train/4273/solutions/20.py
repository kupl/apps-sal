import re


def shorten_to_date(long_date):
    long_date = re.sub(", \d\d[pa]m", "", long_date)
    long_date = re.sub(", \d[ap]m", "", long_date)
    return long_date
