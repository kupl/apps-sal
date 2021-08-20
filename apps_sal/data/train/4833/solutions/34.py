def replace_exclamation(string):
    result = ''
    for char in string:
        if char in 'aeiouAEIOU':
            result += '!'
        else:
            result += char
    return result
