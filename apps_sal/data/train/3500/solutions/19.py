def remove_exclamation_marks(s):
    word = ''
    for let in s:
        if let != '!':
            word = word + let
    return word
