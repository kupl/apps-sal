import re


def shorten_to_date(long_date):
    return re.sub(', ([1-9]|1[0-2])[ap]m', "", long_date)
