import re


def solve(eq):
    return "".join(re.split("([*+-/])", eq)[::-1])
