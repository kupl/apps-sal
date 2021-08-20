def correct(string):
    letters = [i for i in string]
    for i in letters:
        if i == '5':
            letters[letters.index(i)] = 'S'
        elif i == '0':
            letters[letters.index(i)] = 'O'
        elif i == '1':
            letters[letters.index(i)] = 'I'
    return ''.join(letters)
