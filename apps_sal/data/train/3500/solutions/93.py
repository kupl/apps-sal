def remove_exclamation_marks(Str):
    Word = ''
    for s in Str :
        if not s == '!' :
            Word += s
    return Word
