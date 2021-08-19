def replace_exclamation(s):
    remove = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in remove:
        s = s.replace(i, '!')
    return s
