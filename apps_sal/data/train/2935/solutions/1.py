import re


def is_vowel(s):
    regex = '^[aeiou]{1}$'
    return bool(re.match(regex, re.escape(s), re.IGNORECASE))
