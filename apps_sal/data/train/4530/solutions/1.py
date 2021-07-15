import re

def consonant_count(s):
    return len(re.sub(r'[aeiou\d\s\W\_]', '', s))
