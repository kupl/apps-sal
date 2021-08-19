def conjugate(verb):
    conj = {'ar': ('o', 'as', 'a', 'amos', 'ais', 'an'), 'er': ('o', 'es', 'e', 'emos', 'eis', 'en'), 'ir': ('o', 'es', 'e', 'imos', 'is', 'en')}
    return {verb: [verb[:-2] + c for c in conj[verb[-2:]]]}
