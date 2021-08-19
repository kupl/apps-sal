import re


def step_through_with(s):
    # You can't bring your code, but you can bring this comment
    return bool(re.search(r'(.)\1', s))
