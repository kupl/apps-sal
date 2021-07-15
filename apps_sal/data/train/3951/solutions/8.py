from collections import Counter

def duplicate_count(text):
    return sum(v > 1 for v in Counter(text.lower()).values())

