def replace_exclamation(s):
    new = ''
    for i in s:
        if i.lower() not in 'aeiou':
            new += i
        else:
            new += '!'
    return new
