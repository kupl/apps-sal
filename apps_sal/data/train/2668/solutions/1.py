import re


def step_through_with(s):
    return re.compile('([a-z])\\1', re.I).search(s) is not None
