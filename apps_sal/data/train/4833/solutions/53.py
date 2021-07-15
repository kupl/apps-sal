def replace_exclamation(s):
    vowels = "AaEeIiOoUu"
    for x in s:
        if x in vowels:
            s = s.replace(x, '!')
    return s
