from collections import Counter

def only_duplicates(string):
    counts = Counter(string)
    return ''.join(c for c in string if counts[c] > 1)
