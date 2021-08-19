conjugators = {'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'], 'er': ['o', 'es', 'e', 'emos', 'eis', 'en'], 'ir': ['o', 'es', 'e', 'imos', 'is', 'en']}


def conjugate(verb):
    (root, suffix) = (verb[:-2], verb[-2:])
    cs = conjugators[suffix]
    return {verb: [root + c for c in cs]}
