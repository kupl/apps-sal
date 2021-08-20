import re


def consonant_count(s):
    return len(re.sub('[aeiou\\d\\s\\W\\_]', '', s))
