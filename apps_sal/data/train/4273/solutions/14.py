import re


def shorten_to_date(long_date):
    return re.sub(',\\s[0-9]+pm|,\\s[0-9]+am', '', long_date)
