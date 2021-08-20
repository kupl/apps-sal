import re
from collections import Counter


def top_3_words(text):
    words = re.findall("[a-z']*[a-z]+[a-z']*", text.lower())
    top_3 = Counter(words).most_common(3)
    return [tup[0] for tup in top_3]
