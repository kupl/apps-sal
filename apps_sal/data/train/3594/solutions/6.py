from collections import Counter
def is_isogram(word):
    if not isinstance(word, str): return False
    counts = Counter(filter(str.isalpha, word.lower()))
    return bool(counts) and min(counts.values()) == max(counts.values())
