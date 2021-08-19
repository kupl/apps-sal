def replace_exclamation(s):
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for n in s:
        if n in v:
            s = s.replace(n, '!')
    print(s)
    return s
