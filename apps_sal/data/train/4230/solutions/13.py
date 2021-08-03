def reverse_letter(string):
    new_string = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in string:
        if i in alphabet:
            new_string += i
    return new_string[::-1]
