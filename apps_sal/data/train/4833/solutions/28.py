VOWELS = 'aeiouAEIOU'


def replace_exclamation(s):
    #import re
    # return re.sub('[{}]'.format(VOWELS), '!', s)
    # return ''.join('!' if c in VOWELS else c for c in s)
    return s.translate(str.maketrans(VOWELS, len(VOWELS) * '!'))
