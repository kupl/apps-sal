SUFFIXES = {'a': ['o', 'as', 'a', 'amos', 'ais', 'an'], 'e': ['o', 'es', 'e', 'emos', 'eis', 'en'], 'i': ['o', 'es', 'e', 'imos', 'is', 'en']}


def conjugate(verb):
    return {verb: [verb[:-2] + s for s in SUFFIXES[verb[-2]]]}
