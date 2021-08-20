import re


def seven_ate9(s):
    return re.sub('(?<=7)9(?=7)', '', s)
