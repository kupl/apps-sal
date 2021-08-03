def replace_exclamation(s):
    vowel = 'aeiou'
    return ''.join(['!' if x.lower() in vowel else x for x in s])
