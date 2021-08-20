import re


def next_happy_year(year):
    return year + 1 if re.match('(?:([0-9])(?!.*\\1)){4}', str(year + 1)) else next_happy_year(year + 1)
