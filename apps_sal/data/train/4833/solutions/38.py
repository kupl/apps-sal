def replace_exclamation(s):
    vow = 'aeiou'
    ar = []
    for i in s:
        if i.lower() in vow:
            i = '!'
        ar.append(i)
    return ''.join(ar)
