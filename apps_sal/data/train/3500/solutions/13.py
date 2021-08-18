import string


def remove_exclamation_marks(s):
    d = {"!": None}
    t = str.maketrans(d)
    return s.translate(t)
