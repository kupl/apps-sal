import re


def short_form(s):
    return s[0] + re.sub('[aeiou]', '', s[1:-1], flags=re.I) + s[-1]
