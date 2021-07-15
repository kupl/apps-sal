def make_acronym(phrase):
    if isinstance(phrase, str):
        words = phrase.split()
        if all(x.isalpha() or x.isspace() for x in words):
            return ''.join(x[0] for x in words).upper()
        else:
            return 'Not letters'
    return 'Not a string'
