def validate_word(w):
    return len(set((w.lower().count(e) for e in set(w.lower())))) == 1
