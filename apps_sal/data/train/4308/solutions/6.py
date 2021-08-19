def make_acronym(phrase):
    if not isinstance(phrase, str):
        return 'Not a string'
    words = phrase.split()
    if not all((i.isalpha() for i in words)):
        return 'Not letters'
    return ''.join((p[0] for p in words)).upper()
