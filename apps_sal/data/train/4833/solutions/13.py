def replace_exclamation(s):
    return ''.join(['!' if x in ('aeiouAEIOU') else x for x in s])
