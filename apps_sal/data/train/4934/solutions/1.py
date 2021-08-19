def sort(words):
    from random import choice
    from itertools import chain
    words = list(words)
    if len(words) <= 1:
        return iter(words)
    pivot = choice(words)
    return chain(sort((w for w in words if w < pivot)), [pivot], sort((w for w in words if w > pivot)))
