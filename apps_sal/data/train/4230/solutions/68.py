def reverse_letter(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for letter in string:
        if letter in alphabet:
            s = letter + s
    return s
