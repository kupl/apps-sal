VOWELS = 'aeiouAEIOU'


def replace_exclamation(s):
    return s.translate(str.maketrans(VOWELS, len(VOWELS) * '!'))
