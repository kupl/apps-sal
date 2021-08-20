def correct(string):
    value = {'0': 'O', '5': 'S', '1': 'I'}
    result = ''
    for letter in string:
        if value.get(letter):
            result = result + value[letter]
        else:
            result = result + letter
    return result
