def replace_exclamation(s):
    r = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    a = list(s)
    b = []
    for x in a:
        if x in r:
            b.append('!')
        else:
            b.append(x)
    return ''.join(b)
