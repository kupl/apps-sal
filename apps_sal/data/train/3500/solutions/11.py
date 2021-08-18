def remove_exclamation_marks(s):
    return "".join(filter(lambda x: x.isalpha() or x == " " or x == ",", s))
