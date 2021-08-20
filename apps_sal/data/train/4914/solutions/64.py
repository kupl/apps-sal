def position(letter):
    print(letter)
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for (i, elem) in enumerate(alph):
        if elem == letter:
            return f'Position of alphabet: {i + 1}'
