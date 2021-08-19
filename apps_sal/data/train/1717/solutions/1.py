import re
from collections import Counter


def top_3_words(t):
    return [w for (w, c) in Counter(re.findall("'*[a-z][a-z']*", t.lower())).most_common(3)]
