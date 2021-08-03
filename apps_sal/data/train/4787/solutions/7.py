def remove(s):
    s = list(s)
    exclamations = ''
    # look for any exlamations remove and add to exclamations
    while '!' in s:
        s.remove('!')
        exclamations += '!'
    # put string back together and add the exclamations
    return ''.join(s) + exclamations
