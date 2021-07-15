def replace_exclamation(s):
    for char in s:
        if char.lower() in 'aeiou':
            s = s.replace(char, '!')
    return s
