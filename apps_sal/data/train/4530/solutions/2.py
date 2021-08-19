import re


def consonant_count(s):
    return len(re.sub('[^b-df-hj-np-tv-z]', '', s, flags=re.I))
