def replace_exclamation(s):
    word = ''
    for letter in s:
        if letter in 'aeiouAEIOU':
            word += '!'
        else:
            word += letter
    return word
