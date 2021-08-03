def sortme(words):
    words_sorted = sorted(words, key=lambda s: s.casefold())
    return words_sorted
