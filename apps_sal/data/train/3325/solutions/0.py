from collections import Counter

def most_common(s):
    count = Counter(s)
    return ''.join(sorted(s, key=lambda c: -count[c]))
