def replace_exclamation(s):
    return ''.join((el if el not in 'aeiouAEIOU' else '!' for el in s))
