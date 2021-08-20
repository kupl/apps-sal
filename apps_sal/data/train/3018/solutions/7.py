import re
from collections import Counter
EXCLUDE = {'a', 'the', 'on', 'at', 'of', 'upon', 'in', 'as'}


def word_count(s):
    return sum((v for (k, v) in Counter(re.findall('(?i)[a-z]+', s.lower())).items() if k not in EXCLUDE))
