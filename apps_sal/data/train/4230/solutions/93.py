def reverse_letter(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    x =''
    for letter in string:
        if letter in alphabet:
            x += letter
    return x[::-1]


