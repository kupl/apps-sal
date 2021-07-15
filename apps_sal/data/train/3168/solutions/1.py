from collections import Counter

def grabscrab(word, possible_words):
    ws = Counter(word)
    return [s for s in possible_words if Counter(s) == ws]
