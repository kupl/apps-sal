def nth_char(words):
    return ''.join((word[i] for (i, word) in enumerate(words)))
