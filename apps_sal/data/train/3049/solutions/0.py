import re


def textin(txt):
    return re.sub('(two|too|to)', '2', txt, flags=re.I)
