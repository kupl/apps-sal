from collections import Counter
from operator import itemgetter


def letter_frequency(text):
    items = Counter(c for c in text.lower() if c.isalpha()).items()
    return sorted(
        sorted(items, key=itemgetter(0)),
        key=itemgetter(1),
        reverse=True
    )
