def remove_exclamation_marks(s):
    return ''.join([i for i in s if ord(i) != 33])
