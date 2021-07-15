import re


def group_check(brackets):
    while any(pair in brackets for pair in ("{}", "[]", "()")):
        brackets = re.sub(r"{}|\[]|\(\)", "", brackets)
    return not brackets
