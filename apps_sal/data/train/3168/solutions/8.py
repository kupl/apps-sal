def grabscrab(word, possible_words):
    s = sorted(word)
    l = len(word)
    return [w for w in possible_words if len(w) == l and sorted(w) == s]
