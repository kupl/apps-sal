def correct(s):
    mapping = str.maketrans({'0': 'O', '1': 'I', '5': 'S'})
    return s.translate(mapping)
