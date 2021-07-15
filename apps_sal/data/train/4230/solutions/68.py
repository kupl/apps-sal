def reverse_letter(string):
    #do your magic here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for letter in string:
        if letter in alphabet: 
            s = letter + s
    
    return s
