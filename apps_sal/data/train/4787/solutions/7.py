def remove(s):
    s = list(s)
    exclamations = ''
    while '!' in s:
        s.remove('!')
        exclamations += '!'
    return ''.join(s) + exclamations
