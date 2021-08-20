import re


def get_age(s):
    return int(re.search('\\d+', s).group(0))
