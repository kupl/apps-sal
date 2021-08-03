from collections import Counter
from string import ascii_lowercase as alphabet


def missing_alphabets(s):
    counts = Counter(s)
    max_count = max(counts.values())
    return ''.join(c * (max_count - counts[c]) for c in alphabet)
