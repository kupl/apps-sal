def replace_exclamation(s):
    newS = ''
    vowels = 'aeiouAEIOU'
    for letters in s:
        if letters in vowels:
            newS += '!'
        else:
            newS += letters
    return newS
