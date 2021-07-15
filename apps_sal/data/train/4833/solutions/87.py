def replace_exclamation(string):
    Glas = ['a','e','i','o','u','A','E','I','O','U']
    newString = ''
    for s in string:
        if s in Glas:
            newString = newString + '!'
        else:
            newString = newString + s
    return newString
