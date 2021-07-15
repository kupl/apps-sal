def replace_exclamation(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new_s = ''
    for i in s:
        if i in vowels:
            new_s += '!'
        else:
            new_s += i
    return new_s
