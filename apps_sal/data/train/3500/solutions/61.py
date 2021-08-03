def remove_exclamation_marks(s):
    return ''.join(i if i != '!' else '' for i in s)
