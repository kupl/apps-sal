import re


def reverse(stg):
    return re.sub('(([a-zA-Z])\\2+)', lambda m: m.group(1).swapcase(), stg)
