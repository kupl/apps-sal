import re


def prime_string(s):
    return not not re.sub('^(.+)\\1+$', '', s)
