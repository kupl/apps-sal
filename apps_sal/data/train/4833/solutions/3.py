def replace_exclamation(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for a in s:
        if a in vowels:
            s = s.replace(a,'!')
    print(s)
    return s
