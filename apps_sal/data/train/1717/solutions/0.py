from collections import Counter
import re


def top_3_words(text):
    c = Counter(re.findall("[a-z']+", re.sub(" '+ ", ' ', text.lower())))
    return [w for (w, _) in c.most_common(3)]
