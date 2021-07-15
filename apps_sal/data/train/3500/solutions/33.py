def remove_exclamation_marks(s):
    return s.translate(str.maketrans({'!': ''}))
