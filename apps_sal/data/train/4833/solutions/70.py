def replace_exclamation(s):
    st = ''
    for c in s:
        if c in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            st += '!'
        else:
            st += c
    return st
