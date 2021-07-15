def replace_exclamation(s):
    t = str.maketrans('aeiouAEIOU', '!!!!!!!!!!')
    return s.translate(t)
