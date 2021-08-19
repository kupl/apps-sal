def replace_exclamation(s):
    x = []
    for i in range(len(s)):
        if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            x.append('!')
        else:
            x.append(s[i])
    return ''.join(x)
