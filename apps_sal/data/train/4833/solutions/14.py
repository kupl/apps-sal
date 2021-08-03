def replace_exclamation(s):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for c in s:
        if c.lower() in vowels:
            s = s.replace(c, "!")
    return s
