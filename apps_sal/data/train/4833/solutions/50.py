vowels = 'aeiouAEIOU'


def replace_exclamation(s):
    return ''.join(c if c not in vowels else '!' for c in s)
