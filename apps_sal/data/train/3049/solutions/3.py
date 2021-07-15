import re


def textin(stg):
    return re.sub(r"too|two|to", "2", stg, flags=re.I)
