import re


def replace_exclamation(s):
    return re.sub('[aeiou]', '!', s, flags=re.IGNORECASE)
