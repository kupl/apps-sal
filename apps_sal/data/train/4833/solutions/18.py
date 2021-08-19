def replace_exclamation(s):
    vowels = set('aeiouAEIOU')
    return ''.join(('!' if a in vowels else a for a in s))
