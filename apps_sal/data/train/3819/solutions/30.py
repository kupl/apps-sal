def smash(words):
    return ''.join((i + ' ' if len(words) - 1 != n else i for (n, i) in enumerate(words)))
