def correct(string):
    return ''.join(({'5': 'S', '0': 'O', '1': 'I'}.get(l, l) for l in string))
