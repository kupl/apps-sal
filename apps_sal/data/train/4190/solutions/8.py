import re


def is_alt(s):
    return bool(re.search('^([aeiou][^aeiou])*[aeiou]?$|^([^aeiou][aeiou])*[^aeiou]?$', s))
