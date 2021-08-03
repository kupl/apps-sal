def remove_exclamation_marks(s):
    return "".join(filter(lambda char: char != "!", list(s)))
