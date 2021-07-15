def conjugate(verb):
    d = {'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
         'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
         'ir': ['o', 'es', 'e', 'imos', 'is', 'en']}
    return {verb: [verb[:-2] + v for v in d[verb[-2:]]]}
