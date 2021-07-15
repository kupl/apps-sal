import collections

def is_isogram(word):
    if not isinstance(word, str) or not word: return False
    counter = collections.Counter(c for c in word.lower() if c.isalpha())
    return len(set(count for c, count in counter.items())) == 1
