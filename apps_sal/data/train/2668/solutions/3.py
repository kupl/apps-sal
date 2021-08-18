import re


def step_through_with(s):
    return bool(re.search(r'(.)\1', s))
