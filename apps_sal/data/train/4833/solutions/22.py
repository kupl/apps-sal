def replace_exclamation(s):
    for ch in 'AaEeIiOoUu':
        s = s.replace(ch, "!")
    return s
