def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)
