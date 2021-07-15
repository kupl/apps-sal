def grabscrab(word, possible_words):
    ws = sorted(word)
    return [w for w in possible_words if sorted(w) == ws]
