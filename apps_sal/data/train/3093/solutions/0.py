import re


def insert_dash(num):
    return re.sub('([13579])(?=[13579])', '\\1-', str(num))
