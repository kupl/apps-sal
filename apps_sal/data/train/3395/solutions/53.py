def remove_duplicate_words(s):
    return ' '.join((i for (loop, i) in enumerate(s.split()) if s.split().index(i) == loop))
