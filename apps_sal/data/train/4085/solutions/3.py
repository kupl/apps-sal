import random
import re

def sub(m):
    s = m.group()
    xs = list(s[1:-1])
    mid = list(s[1:-1])
    while mid == xs:
        random.shuffle(mid)
    return s[0] + ''.join(mid) + s[-1]

def mix_words(s):
    if not isinstance(s, str):
        return None
    return re.sub('[a-z]{4,}', sub, s, flags=re.I)
