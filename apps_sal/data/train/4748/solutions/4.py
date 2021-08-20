import re


def insert_dash2(num):
    a = re.sub('([2468])(?=[2468])', '\\1*', str(num))
    return re.sub('([13579])(?=[13579])', '\\1-', a)
