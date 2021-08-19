import re


def is_letter(stg):
    return bool(re.match('[a-z]\\Z', stg, re.I))
