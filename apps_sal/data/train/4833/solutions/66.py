def replace_exclamation(s):
    strx = ''
    for x in s:
        if x.lower() in 'aeiou':
            strx += '!'
        else:
            strx += x
    return strx
