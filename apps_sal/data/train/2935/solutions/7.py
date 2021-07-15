import re
PATTERN = re.compile('[eaiou]', flags=re.I)
def is_vowel(s): 
    return bool(PATTERN.fullmatch(s))
