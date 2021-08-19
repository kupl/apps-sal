def correct(string):
    letters = {'5': 'S', '0': 'O', '1': 'I'}
    return ''.join((letters[x] if x.isdigit() else x for x in string))
