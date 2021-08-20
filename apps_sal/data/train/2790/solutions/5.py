import re


def dup(lst):
    return [re.sub('(.)\\1+', '\\1', stg) for stg in lst]
