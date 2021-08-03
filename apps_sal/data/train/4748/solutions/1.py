import re


def insert_dash2(num):
    s = str(num)
    s = re.sub('(?<=[13579])(?=[13579])', '-', s)
    s = re.sub('(?<=[2468])(?=[2468])', '*', s)
    return s
