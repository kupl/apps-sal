def replace_exclamation(s):
    replace_chars = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char in replace_chars:
        s = s.replace(char, "!")
    return s
