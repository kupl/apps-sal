def insert_missing_letters(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new = ''
    used = ''
    for letter in set(word):
        alphabet = alphabet.replace(letter, '')
    for letter in word:
        if letter not in used:
            new += letter + ''.join([x.upper() for x in alphabet if ord(x) > ord(letter)])
        else:
            new += letter
        used += letter
    return new
