import re


def step_through_with(s):
    return bool(re.search('(.)\\1', s))
