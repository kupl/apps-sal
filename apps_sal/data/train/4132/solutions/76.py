import re


def correct_tail(body, tail):
    sub = re.sub('.', '', body, len(body) - len(tail))
    if sub == tail:
        return True
    else:
        return False
