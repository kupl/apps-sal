def conjugate(verb):
    base, infinitive_suffix = verb[:-2], verb[-2:]
    patterns = {'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'], 'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
                'ir': ['o', 'es', 'e', 'imos', 'is', 'en']}
    conjugations = [base + suffix for suffix in patterns[infinitive_suffix]]
    return {verb: conjugations}
