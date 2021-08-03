def make_acronym(phrase):
    import re
    if type(phrase) is not str:
        return 'Not a string'
    if re.search(r'[^A-Za-z\s]', phrase):
        return 'Not letters'
    acronym = ''
    for x in phrase.split():
        acronym += x[0]
    return acronym.upper()
