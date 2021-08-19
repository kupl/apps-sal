import re


def insert_dash(num):
    return re.sub('[13579](?=[13579])', '\\g<0>-', str(num))
