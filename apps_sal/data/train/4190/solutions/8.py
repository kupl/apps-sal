import re


def is_alt(s):
    return bool(re.search(r'^([aeiou][^aeiou])*[aeiou]?$|^([^aeiou][aeiou])*[^aeiou]?$', s))
