import re


def textin(stg):
    return re.sub('too|two|to', '2', stg, flags=re.I)
