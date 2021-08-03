def replace_exclamation(x):
    a = ''
    for i in x:
        if i.lower() in 'aeiou':
            a += '!'
        else:
            a += i
    return a
