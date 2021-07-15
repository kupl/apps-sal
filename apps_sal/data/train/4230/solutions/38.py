def reverse_letter(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    newString = ''
    for letter in string:
        if letter in alphabet:
            newString += letter
        else:
            continue
    return newString[::-1]


