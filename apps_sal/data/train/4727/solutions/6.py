import re


def remove_vowels(strng):
    return re.sub('[aeiou]', '', strng, flags=re.I)
