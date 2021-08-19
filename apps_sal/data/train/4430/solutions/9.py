import re


def vowel_2_index(string):
    return re.sub('[aeiou]', lambda m: str(m.start(0) + 1), string, flags=re.IGNORECASE)
