import re


def consonant_count(s):
    return len(re.sub(r'[^b-df-hj-np-tv-z]', '', s, flags=re.I))
