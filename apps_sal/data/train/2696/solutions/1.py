import re


def prime_string(s):
    return not not re.sub(r"^(.+)\1+$", "", s)
