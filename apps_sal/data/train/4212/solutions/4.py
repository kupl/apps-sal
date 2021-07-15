from itertools import chain

def unite_unique(*lists):
    cache = set()
    result = list()
    for elem in chain(*lists):
        if elem not in cache:
            result.append(elem)
        cache.add(elem)
    return result
