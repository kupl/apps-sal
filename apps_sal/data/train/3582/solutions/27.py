import re


def is_digit(n):
    # your code here

    return True if not re.match(r"^\d$", n, re.M) is None and len(n) == 1 else False
