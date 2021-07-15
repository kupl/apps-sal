def grabscrab(word, possible):
    sw = sorted(word)
    return [w for w in possible if sorted(w) == sw]
