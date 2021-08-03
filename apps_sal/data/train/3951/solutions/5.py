from collections import Counter


def duplicate_count(text):
    counter = Counter(text.lower())
    return len([list(counter.keys()) for i in list(counter.values()) if i > 1])
