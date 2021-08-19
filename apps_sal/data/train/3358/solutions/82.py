def correct(string):
    return ''.join(['OSI'['051'.index(c)] if c in '051' else c for c in string])
