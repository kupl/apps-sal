import re


def is_alt(s):
    return False if re.findall('[aeiou0]{2,}|[^aeiou0-9\\W]{2,}', s) else True
