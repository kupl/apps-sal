from operator import itemgetter


def make_acronym(phrase):
    if type(phrase) != str:
        return 'Not a string'
    if not all((c.isalpha() or c.isspace() for c in phrase)):
        return 'Not letters'
    return ''.join(map(itemgetter(0), phrase.split())).upper()
